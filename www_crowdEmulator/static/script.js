$('document').ready(function () {

    $('.dpad_down').click(function () {
        ajaxPost('down');
    });
    $(".dpad_left").click(function () {
        ajaxPost('left');
    });
    $(".dpad_right").click(function () {
        ajaxPost('right');
    });
    $(".dpad_up").click(function () {
        ajaxPost('up');
    });
    $('#select').click(function () {
        ajaxPost('select');
    });
    $('#start').click(function () {
        ajaxPost('start');
    });
    $('#button_a').click(function () {
        ajaxPost('a');
    });
    $('#button_b').click(function () {
        ajaxPost('down');
    });

});

function ajaxPost($input) {
    $.ajax
    ({
        url: '/input',
        data: { 'input': $input, 'userid': 'userid_var' },
        type: 'post',
        success: function (response) {
            console.log(response.message);
        }
    });
    console.log("jQuery loaded and you clicked " + $input);
}