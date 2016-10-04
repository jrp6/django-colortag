Django colortag
================

Bare tools to help building data tagging models.
Used for example in A+ and MOOC-Jutut projects to tag feedbacks or users with colorful tags.
Project builds on top of Django and django-html5-colorfield.

Remember to include stylesheet in your template files:

```html+django
{% load static %}

<!-- TODO: load bootstrap v3 css here too -->
<!-- stylesheets for django colortags to show correctly -->
<link rel="stylesheet" href="{% static "django_colortag.css" %}">

<!-- TODO: load jquery here too -->
<!-- Supporting javascript. Only needed for django_colortag_choice below -->
<script src="{% static "django_colortag.js" %}">
```

Also for bootstrap tooltips to work, you need this kind of js snipet:

```javascript
$(function() {
  $('.colortag[data-toggle="tooltip"]').tooltip();
  $('.colortag-choice').each(django_colortag_choice); /* only needed if you use ColortagChoiceFilter, ColortagChoiceField or ColortagSelectMultiple */
});
```

You can render colortag in your templates like this:

```html+django
{{ tag.render_as_button }}
<!-- or -->
{% load colortag %}
{{ tag|colortag_button }}
```

You can use colortags in filters like

```python
import django_filters
from django_colortag.filters import ColortagChoiceFilter

class TagFilter(django_filters.FilterSet):
    tags = ColortagChoiceFilter()
```

For any of the above to work remember to add `django_colortag` into your django settings `INSTALLED_APPS`.
