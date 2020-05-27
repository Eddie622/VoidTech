$( document ).ready(function() {
    // place feather icons
    feather.replace()

    // Stop dropdown from closing on click within container
    $('.dropdown-menu').click(function(e) {
        e.stopPropagation();
    });
});