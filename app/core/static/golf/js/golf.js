jQuery(document).ready(function($) {
    $(".clickable-obj").click(function() {
        window.location = $(this).data("href");
    });
});
