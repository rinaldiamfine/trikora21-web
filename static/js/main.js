var DEFAULT_FEATURE = ['feature-tracking', 'feature-calculator', 'feature-order', 'feature-profile', 'feature-setting'];

$(document).ready(function () { 
    $(".evaline-feature").click(function() {
        var featureId = this.id;
        setFeatureSelected(featureId);
    });

    $(".action-dashboard-next").click(function() {
        var selectedFeatureId = $('.evaline-feature.is-active');
        var dataLink = selectedFeatureId.attr('data-href');
        window.location = dataLink;
    });
    $(".action-dashboard-previous").click(function() {
        console.log("BUTTON PREVIOUS");
    });

    $(".profile-list").click(function() {
        var profileId = this.attributes['data-href'].value;
        var profileLink = window.location + '/' + String(profileId);
        window.location = profileLink;
    })
});

function setFeatureSelected(Id) {
    for(var i=0; i<DEFAULT_FEATURE.length; i++) {
        try {
            if (DEFAULT_FEATURE[i] != Id) {
                $('#'+DEFAULT_FEATURE[i]).removeClass('is-active');
            }
            else {
                $('#'+DEFAULT_FEATURE[i]).addClass('is-active');
            }
        }
        catch(err) {

        }
    }
}

var inputCalendar = $('input.is-calendar');
if (inputCalendar.length > 0) {
    if (inputCalendar.length == 1) {
        if (inputCalendar[0].attributes.value) {
            var calendars = bulmaCalendar.attach('[type="date"]', {startDate: new Date(inputCalendar[0].attributes.value.value)});
        }
        else {
            var calendars = bulmaCalendar.attach('[type="date"]');
        }
    }
    else {
        var calendars = bulmaCalendar.attach('[type="date"]');
    }
}
else {
    var calendars = bulmaCalendar.attach('[type="date"]');
}

// Loop on each calendar initialized
for(var i = 0; i < calendars.length; i++) {
    // Add listener to select event
	calendars[i].on('select', date => {
		console.log(date);
	});
}

// To access to bulmaCalendar instance of an element
var element = document.querySelector('#my-element');
if (element) {
	// bulmaCalendar instance is available as element.bulmaCalendar
	element.bulmaCalendar.on('select', function(datepicker) {
		console.log(datepicker.data.value());
	});
}