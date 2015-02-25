package demo

import (
	"appengine"
	"appengine/datastore"
	"github.com/go-martini/martini"
	"github.com/martini-contrib/binding"
	"github.com/martini-contrib/render"
	"math"
	"net/http"
	"strings"
)

type Book struct {
	Handle   string
	Filename string  `form:"filename"`
	Url      string  `form:"url"`
	Size     float64 `form:"size"`
}

func (book *Book) Key(c appengine.Context) *datastore.Key {
	items := strings.Split(book.Url, "/")
	book.Handle = items[len(items)-1]
	c.Errorf("Book: %v", book)
	return datastore.NewKey(c, "Book", book.Handle, 0, nil)
}

func (book *Book) Save(c appengine.Context) (*datastore.Key, error) {
	book.Size = Round(book.Size/1024/1024, 2, 2)
	return datastore.Put(c, book.Key(c), book)
}

func init() {
	m := martini.Classic()
	m.Use(render.Renderer())

	m.Use(render.Renderer(render.Options{
		Directory:  "templates",
		Extensions: []string{".html"},
		Charset:    "UTF-8",
	}))

	m.Get("/", List_Books)
	m.Post("/books", binding.Form(Book{}), Add_Book)
	m.Get("/books", List_Books)
	m.Get("/books/:handle", Show_Book)
	m.Delete("/books/:handle", Remove_Book)

	http.Handle("/", m)

}

func Add_Book(book Book, r render.Render, req *http.Request) {
	c := appengine.NewContext(req)
	book.Save(c)
	r.JSON(200, []string{book.Handle})
}

func List_Books(r render.Render, req *http.Request) {
	c := appengine.NewContext(req)
	books := []Book{}

	datastore.NewQuery("Book").GetAll(c, &books)

	r.HTML(200, "index", books)
}

func Show_Book(params martini.Params, r render.Render, req *http.Request) {
	c := appengine.NewContext(req)
	books := []Book{}

	datastore.NewQuery("Book").Filter("Handle=", params["handle"]).Limit(1).GetAll(c, &books)

	r.HTML(200, "book", books[0])
}

func Remove_Book(params martini.Params, r render.Render, req *http.Request) {
	c := appengine.NewContext(req)

	key := datastore.NewKey(c, "Book", params["handle"], 0, nil)
	datastore.Delete(c, key)

	r.JSON(200, []string{})
}

func Round(val float64, roundOn float64, places int) (newVal float64) {
	var round float64
	pow := math.Pow(10, float64(places))
	digit := pow * val
	_, div := math.Modf(digit)
	if div >= roundOn {
		round = math.Ceil(digit)
	} else {
		round = math.Floor(digit)
	}
	newVal = round / pow
	return
}
