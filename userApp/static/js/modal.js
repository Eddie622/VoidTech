// TODO: Use specs instead of description in modal

$(document).ready(function () {
    // feather icon placement
    feather.replace();
    
    // Modal functionality
    $('#exampleModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal

        // Extract Data
        var name = button.data('title')
        var desc = button.data('desc')

        // Set-up Modal
        var modal = $(this)
        modal.find('.modal-title').text(name)
        modal.find('.modal-body').text("PLACEHOLDER FOR SPECS: " + desc)
    })
});