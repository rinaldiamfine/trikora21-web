$(document).ready(function () {    
    //Navbar Clone
    if ($('#navbar-clone').length) {
        $(window).scroll(function () {    // this will work when your window scrolled.
            var height = $(window).scrollTop();  //getting the scrolling height of window
            if (height > 70) {
                $("#navbar").addClass('set-inactive');
                $("#navbar-clone").removeClass('set-inactive');
            } else {
                $("#navbar").removeClass('set-inactive');
                $("#navbar-clone").addClass('set-inactive');
            }
        });
    }
})
