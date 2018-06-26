$(function() {
    toolbar = [ 'title', 'bold', 'italic', 'underline', 'strikethrough',
            'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|',
            'link', 'image', 'hr', '|', 'indent', 'outdent' ];
    var editor = new Simditor({
        textarea: $("#id_content"),
        placeholder: "在此编辑你的文章",
        toolbar : toolbar,
        //optional options
    });
});