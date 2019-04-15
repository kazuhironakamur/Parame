from django import template

register = template.Library()

from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
def cut(value, arg):
    "入力から arg の値を全て取り去る"
    return value.replace(arg, '')

"""
https://djangoproject.jp/doc/ja/1.0/howto/custom-template-tags.html
"""
@register.filter
def tab(value):
    esc = conditional_escape

    return mark_safe('<table border="1"><thead><th></th></thead><tbody><tr><td>' +
        esc(value) +
        '</td></tr></tbody></table>')