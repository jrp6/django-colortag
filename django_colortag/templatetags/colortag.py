from django import template
#from django.template.loader import get_template
from django.utils.html import format_html


register = template.Library()



def render_as_button(colortag, extra=None):
    context = {
        'element': 'span',
        'tooltip_trigger': 'hover',
        'tooltip_placement': 'top',
        'size': 'xs',
        'class': '',
        'btn_class': 'btn',
    }
    if extra:
        context.update(extra)
    if context.get('static'):
        context['active'] = True
        context['btn_class'] = ''

    for k in ('pk', 'slug', 'name', 'description', 'color'):
        context['tag_'+k] = getattr(colortag, k)
    context['class'] += ' colortag-dark' if colortag.font_white else " colortag-light"
    if context.get('active'):
        context['class'] += ' colortag-active'

    template = '<{element}'
    if not context.get('no_tooltip'):
        template += (
            ' data-toggle="tooltip"'
            ' data-trigger="{tooltip_trigger}"'
            ' data-placement="{tooltip_placement}"'
            ' data-title="{tag_description}"'
        )
    template += (
        ' title="{tag_description}"'
        ' data-tagpk="{tag_pk}"'
        ' data-tagslug="{tag_slug}"'
        ' data-hovercolor="{tag_color}"'
        ' class="{btn_class} label label-{size} colortag {class}"'
        ' style="background-color: {tag_color};"'
        '>'
        '{tag_name}'
        '</{element}>'
    )

    return format_html(template, **context)

@register.filter
def colortag_button(colortag, options=''):
    extra = {}
    for option in options.split(','):
        parts = option.split('=', 1)
        name, val = parts if len(parts) == 2 else (parts[0], True)
        extra[name] = val

    return render_as_button(colortag, extra)
