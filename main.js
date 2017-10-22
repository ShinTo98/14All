$(document).ready(function() {
	$("#buy_button").click(function() {
		$("#main_page").animate({top: '0px'}, 0);
		$("#main_page").fadeOut('slow');
		$("#buy_page").fadeIn(1200);
	});
});
