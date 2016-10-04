def get_colortag_attrs(colortag, options):
    attrs = {
        'data-tagid': colortag.id,
        'data-tagslug': colortag.slug,
        'style': 'background-color: {};'.format(colortag.color),
    }
    if not options.get('no_tooltip') and colortag.description:
        attrs.update({
            'data-toggle': 'tooltip',
            'data-trigger': options.get('tooltip_trigger', 'hover'),
            'data-placement': options.get('tooltip_placement', 'top'),
            'title': colortag.description,
        })
    return attrs


def get_colortag_classes(colortag, options):
    cls = set(('colortag',))
    cls.add('colortag-dark' if colortag.font_white else 'colortag-light')
    if options.get('active'):
        cls.add('colortag-active')
    if options.get('button'):
        cls.add('btn')
    if options.get('label'):
        cls.update(('label', 'label-{}'.format(options.get('size', 'xs'))))
    if options.get('class'):
        cls.update(options['class'].split(' '))
    return cls
