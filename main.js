$(document).ready(function() {
	$("#buy_button").click(function() {
		$("#main_page").animate({top: '0px'}, 0);
		$("#main_page").fadeOut('slow');
		$("#buy_page").fadeIn(1200);
	});
});

$(document).ready(function() {
	$("#nope_button").click(function() {
		$("#second_page").animate({bottom: '0px'}, 1000);
		$("#first_page").animate({top: '800px'}, 500);
		$("#first_page").fadeOut('slow');
		$("#second_page").fadeIn(1200);
	});
});

$(document).ready(function() {
	$("#rethink_button").click(function() {
		$("#third_page").animate({bottom: '0px'}, 1000);
		$("#second_page").animate({right: '1100px'}, 500);
		$("#second_page").fadeOut('slow');
		$("#third_page").fadeIn(1200);
	});
});