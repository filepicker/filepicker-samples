$(function () {
    filepicker.setKey("SET_YOUR_KEY_HERE");
    $('#book_modal').on('hidden.bs.modal', function () {
	location.reload();
    })
});


function add_book() {
    filepicker.pick(
        {
	    mimetypes: ['application/pdf'],
	    maxSize: 1024 * 1024 * 50
        },
        function(Blob){
	    url = Blob.url;
	    $.post("/books",
		   Blob,
		   function(data){
		       openModal(data[0]);
		   });
        });
}

function save_page(url, page) {
    filepicker.exportFile(
	url+"/convert?page="+page,
	{mimetype:'image/png'},
	function(Blob){
	}
    );
}

function save_book(url) {
    filepicker.exportFile(
	url,
	{
	    mimetype: 'application/pdf'
	},
	function(Blob) {
	}
    );
}

function delete_book(url, handle) {
    $.ajax({
	url: '/books/'+handle,
	type: 'DELETE',
	success: function(result) {
	    $('#file_url').text("Book was deleted. You can go back to the list.")
	    $('#demo_modal_header').text("Success!")
	    $('#book_modal').modal();
	}
    });
}

function openModal(handle) {
    $('#file_url').attr('href', "/books/"+handle);
    $('#file_url').text("You can go to your book now.")
    $('#demo_modal_header').text("Success!")
    $('#book_modal').modal();
};
