from django import template
from django.utils.safestring import mark_safe

register = template.Library()

def cut(value, arg):
    "入力から arg の値を全て取り去る"
    return value.replace(arg, '')

"""
https://djangoproject.jp/doc/ja/1.0/howto/custom-template-tags.html
"""
@register.filter
def tab(value):
    return mark_safe('<table border="1"><thead><th></th></thead><tbody><tr><td>' + value + '</td></tr></tbody></table>')