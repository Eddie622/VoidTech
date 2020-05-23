$( document ).ready(function() {
    // Stop dropdown from closing on click within container
    $('.dropdown-menu').click(function(e) {
        e.stopPropagation();
    });
});