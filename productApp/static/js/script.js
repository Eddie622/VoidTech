$( document ).ready(function() {
    // place feather icons
    feather.replace();

    // Stop dropdown from closing on click within container
    $('.dropdown-menu').click(function(e) {
        e.stopPropagation();
    });

    // Search functionality
    $('#Search').keyup(function(e) {
        e.preventDefault()
        var data = $('.searchForm').serialize()

        $.post("search/", data, function(serverResponse){
                $('#productResults').html(serverResponse);
                feather.replace(); // re-load icons
            }
        )
    })
});