// Reload feather icons, hide generated alerts
function reload(){
    feather.replace();
    $('.add-to-wishlist-alert').hide();
}

$(document).ready(function () {
    // Get initial product content
    $.get("search/", function (serverResponse) {
        $("#productResults").html(serverResponse);
        reload()
    });

    // Stop dropdown from closing on click within container
    $('.dropdown-menu').click(function (e) {
        e.stopPropagation();
    });

    // Show alert when view wishlist button is pressed (close all others)
    // (only applies when no user is logged in) SEE: index.html line-126
    $('.view-wishlist-btn').click(function () {
        $('.alert').hide();
        $('.view-wishlist-alert').show();
    });

    // category functionality (csrf_token needed due to post without form)
    $('.category').click(function () {
        var value = $(this).text()
        var csrftoken = Cookies.get('csrftoken');

        // align text value to category ID of Category model
        switch (value) {
            case 'Desktops':
                value = 1;
                break;
            case 'Laptops':
                value = 2;
                break;
            case 'Tablets':
                value = 3;
                break;
            case 'Phones':
                value = 4;
                break;
            case 'Accessories':
                value = 5;
        }

        // setup data to post
        data = {
            'csrfmiddlewaretoken': csrftoken,
            'category': value
        }

        $.post("search/", data, function (serverResponse) {
            $('#productResults').html(serverResponse);
            reload();
        }
        )
    });

    // Search functionality
    $('#Search').keyup(function (e) {
        e.preventDefault()
        var data = $('.searchForm').serialize()

        $.post("search/", data, function (serverResponse) {
            $('#productResults').html(serverResponse);
            reload();
        }
        )
    })
});

// Open alert when wish icon within product is clicked (close all others)
$(document).on('click', '.displayWish', function(){
    $('.alert').hide();
    $(this).next().show();
});

// Close alert when wish icon within product is clicked
$(document).on('click', '.close', function(){
    $(this).parent().hide();
});