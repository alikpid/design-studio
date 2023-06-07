$(document).ready(function () {
    $('#comment-group').hide();

    $('#status').change(function () {
        let selectedStatus = $(this).val();

        if (selectedStatus === 'Completed') {
            $('#design-image-group').show();
            $('#comment-group').hide();
        } else {
            $('#design-image-group').hide();
            $('#comment-group').show();
        }
    });
});