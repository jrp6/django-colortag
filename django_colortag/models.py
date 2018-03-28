from django.db import models
from django.utils.functional import cached_property
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from colorfield.fields import ColorField
from functools import total_ordering

from .templatetags.colortag import render_as_button
from .utils import gray_tone

MAX_LENGTH = 20


@total_ordering
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

    def __eq__(self, other):
        """Compare slugs if other is a string. Otherwise delegate to super"""
        if isinstance(other, str):
            return self.slug == other
        else:
            return super().__eq__(other)

    def __gt__(self, other):
        """Compare ColorTags by slug"""
        if isinstance(other, ColorTag):
            return self.slug > other.slug
        else:
            return NotImplemented

    def save(self, *args, **kwargs):

        # Default for slug if there is none
        if not self.slug and self.name:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)
