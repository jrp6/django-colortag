Django colortag
================

Bare tools to help building data tagging models.
Used for example in A+ and MOOC-Jutut projects to tag feedbacks or users with colorful tags.
Project builds on top of Django and django-html5-colorfield.

Remember to include stylesheet in your template files:

```html+django
{% load staticfiles %}
<link rel="stylesheet" href="{% static "django_colortag.css" %}">
```

Also for bootstrap tooltips to work, you need this kind of js snipet:

```javascript
$(function() {
  $('.colortag[data-toggle="tooltip"]').tooltip();
});
```

You can render colortag in your templates like this:

```html+django
{% load colortag %}
{{ tag|colortag_button }}
```

For above to work add `django_colortag` in your django projects settings `INSTALLED_APPS` list.
