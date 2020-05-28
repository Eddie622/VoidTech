$(document).ready(function () {
    // place feather icons
    feather.replace();

    // Stop dropdown from closing on click within container
    $('.dropdown-menu').click(function (e) {
        e.stopPropagation();
    });

    // category functionality (csrf_token needed due to post without form)
    $('.category').click(function (e) {
        var value = $(this).text()
        var csrftoken = Cookies.get('csrftoken');

        // align value to category ID of Category model
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

        data = {
            'csrfmiddlewaretoken' : csrftoken,
            'category' : value
        }

        $.post("search/", data, function (serverResponse) {
            $('#productResults').html(serverResponse);
            feather.replace(); // re-load icons
            }
        )
    });

    // Search functionality
    $('#Search').keyup(function (e) {
        e.preventDefault()
        var data = $('.searchForm').serialize()

        $.post("search/", data, function (serverResponse) {
            $('#productResults').html(serverResponse);
            feather.replace(); // re-load icons
            }
        )
    })
});