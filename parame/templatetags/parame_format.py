from django import template
from django.utils.safestring import mark_safe

register = template.Library()

def cut(value, arg):
    "入力から arg の値を全て取り去る"
    return value.replace(arg, '')

@register.filter
def tab(value):
    return mark_safe('<table border="1"><thead><th></th></thead><tbody><tr><td>' + value + '</td></tr></tbody></table>')