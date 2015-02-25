function update(new_page) {
    page = new_page;

    var img = $("<img id='file' alt='' class='img-responsive'/>");
    img.attr("src", url+"/convert?page="+new_page);
    $("#file").replaceWith(img);
    $("#file").show();
}

$("#next").click(function(e){
    update(page + 1);

});

$("#previous").click(function(e) {
    update(page - 1);
});


$(function () {
    var page = 1;
    update(page);
});
