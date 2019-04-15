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

    table = '<table border="1">'
    table += '<thead><th></th><thead>'
    table += '<tbody>'
    for line in value.splitlines():
        table += '<tr>'
        for col in line.split('|'):
            table += '<td>' + col + '</td>'
        table += '</tr>'

    table += '</tbody></table>'
    return mark_safe(table)