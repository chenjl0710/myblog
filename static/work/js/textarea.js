(function () {
    $(function() {
        toolbar = [ 'title', 'bold', 'italic', 'underline', 'strikethrough',
                'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|',
                'link', 'image', 'hr', '|', 'indent', 'outdent' ];
        var editor1 = new Simditor({
            textarea: $("#id_content"),
            placeholder: "在此编辑你的文章",
            toolbar : toolbar,
        });
    });
    $(function() {
        toolbar = [ 'title', 'bold', 'italic', 'underline', 'strikethrough',
                'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|',
                'link', 'image', 'hr', '|', 'indent', 'outdent' ];
        var editor2 = new Simditor({
            textarea: $("#id_lastWeekContent"),
            placeholder: "在此编辑你的文章",
            toolbar : toolbar,
        });
    });
    $(function() {
        toolbar = [ 'title', 'bold', 'italic', 'underline', 'strikethrough',
                'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|',
                'link', 'image', 'hr', '|', 'indent', 'outdent' ];
        var editor2 = new Simditor({
            textarea: $("#id_thisWeekContent"),
            placeholder: "在此编辑你的文章",
            toolbar : toolbar,
        });
    });
    $(function() {
        toolbar = [ 'title', 'bold', 'italic', 'underline', 'strikethrough',
                'color', '|', 'ol', 'ul', 'blockquote', 'code', 'table', '|',
                'link', 'image', 'hr', '|', 'indent', 'outdent' ];
        var editor2 = new Simditor({
            textarea: $("#id_nextWeekContent"),
            placeholder: "在此编辑你的文章",
            toolbar : toolbar,
        });
    });
}).call(this);