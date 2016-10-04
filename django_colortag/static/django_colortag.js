function django_colortag_choice() {
	var $ = jQuery;
	var widget = $(this);
	var bgroup = $('<div></div>');
	widget.after(bgroup);

	/* add button for each checkbox/radio */
	widget.find('input').each(function() {
		var input = $(this);
		var text = input.parent().text().trim();
		var button = $('<button type="button"><i class="glyphicon"></i> '+text+'</button>');
		button.addClass(input.data('class'));
		button.css('background-color', input.css('background-color'));
		bgroup.append('\n');
		bgroup.append(button);

		if (input.is(":radio")) {
			button.on('click', function () {
				input.prop('checked', true);
				input.closest('ul').find('input:radio').each(function() { $(this).triggerHandler('change'); });
			});
		} else {
			button.on('click', function () {
				input.prop('checked', !input.is(':checked'));
				input.triggerHandler('change');
			});
		}

		input.on('change', function () {
			var on = input.is(':checked');
			var icon = 'glyphicon glyphicon-' + (on?'check':'unchecked');
			if (on) {
				button.addClass('colortag-active');
				button.find('.glyphicon').removeClass('glyphicon-unchecked').addClass('glyphicon-check');
			} else {
				button.removeClass('colortag-active');
				button.find('.glyphicon').removeClass('glyphicon-check').addClass('glyphicon-unchecked');
			}
		});

		input.triggerHandler('change');
	});

	/* hide inputs when all buttons have been added */
	widget.hide();
}
