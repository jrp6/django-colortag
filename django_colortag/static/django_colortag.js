function django_colortag_choice() {
	jQuery(this).replaceCheckboxesWithButtons({
		groupClass: 'colortag-container',
		buttonClass: '',
		onicon: 'check',
		officon: 'unchecked',
		nocolor: true,
		buttonSetup: function(input, button, group) {
			button.css('backgroundColor', input.data('background'));
		},
	});
}
