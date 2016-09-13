from django.db import models
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from colorfield.fields import ColorField

from .templatetags.colortag import render_as_button
from .utils import gray_tone

MAX_LENGTH = 20


class ColorTag(models.Model):
    class Meta:
        abstract = True
        ordering = ['slug']

    name = models.CharField(max_length=MAX_LENGTH, help_text=_("Display name for tag"))
    slug = models.SlugField(max_length=MAX_LENGTH, help_text=_("Slug key for tag. If left blank, one is created from name"))
    description = models.CharField(max_length=155, blank=True, help_text=_("Describe the usage or meaning of this tag"))
    color = ColorField(default="#CD0000", help_text=_("Color that is used as background for this tag"))

    @cached_property
    def color_gray_tone(self):
        return gray_tone(self.color)

    @cached_property
    def color_gray_tone_edge(self):
        return not (0.1 < self.color_gray_tone < 0.9)

    @cached_property
    def font_white(self):
        return self.color_gray_tone < 0.5

    @cached_property
    def font_color(self):
        return '#FFF' if self.font_white else '#000'

    def render_as_button(self, **options):
        return render_as_button(self, options)

    def __str__(self):
        return 'ColorTag({!r}, {!r}, {!r})'.format(
            self.name, self.slug, self.description
        )
