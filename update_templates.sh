#!/bin/sh

get_hash() {
    hash=$(openssl dgst -sha384 -binary "$1" | openssl base64 -A)
    echo "sha384-$hash"
}

base="django_colortag/static"
js="django_colortag.js"
jsh=$(get_hash "$base/$js")
css="django_colortag.css"
cssh=$(get_hash "$base/$css")

cat > django_colortag/templates/django_colortag.head.html <<TMPL
{% load static %}
<link rel="stylesheet" href="{% static '$css' %}" integrity="$cssh" crossorigin="anonymous">
<script src="{% static '$js' %}" integrity="$jsh" crossorigin="anonymous"></script>
TMPL

cat > django_colortag/templates/django_colortag.head.jinja <<TMPL
<link rel="stylesheet" href="{{ static('$css') }}" integrity="$cssh" crossorigin="anonymous">
<script src="{{ static('$js') }}" integrity="$jsh" crossorigin="anonymous"></script>
TMPL
