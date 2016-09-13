from django import forms
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from .models import ColorTag

class ColorTagForm(forms.ModelForm):
    class Meta:
        model = ColorTag
        fields = (
            'name',
            'slug',
            'description',
            'color',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].required = False

    def clean(self):
        cleaned_data = super().clean() or self.cleaned_data

        name = cleaned_data['name']

        if not cleaned_data.get('slug') and name:
            cleaned_data['slug'] = slugify(name)

        return cleaned_data
