from django.forms import models

from .widgets import ColortagSelectMultiple


class ColortagChoiceField(models.ModelMultipleChoiceField):
    widget = ColortagSelectMultiple

    def label_from_instance(self, obj):
        return obj
