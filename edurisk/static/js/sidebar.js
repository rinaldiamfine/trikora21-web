$(document).ready(function () {

    $(".sidebar-button").click(function() {
        var icon = $('#sidebar-icon');
        var target = $(this).data("target");
        var menu = $('#'+target);
        //ACTIVE
        if (icon.hasClass('fa-times')) {
            menu.hide('fast');
            icon.addClass('fa-bars');
            icon.removeClass('fa-times');
        }
        //INACTIVE
        else {
            menu.show('fast');
            icon.addClass('fa-times');
            icon.removeClass('fa-bars');
        }
        
    });

});