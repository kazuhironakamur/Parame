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

    max_cols_count = 0
    for line in esc(value).splitlines():
        cols_count = len(line.split('|'))
        if max_cols_count < cols_count:
            max_cols_count = cols_count

    table = '<table border="1">'
    table += '<thead><th colspan="' + str(max_cols_count) +  '">Parameter Sheet</th><thead>'
    table += '<tbody>'
    for line in esc(value).splitlines():
        row = '<tr>'
        cols_count = len(line.split('|'))
        for col in line.split('|'):
            span = max_cols_count - cols_count + 1
            if span > 1:
                row += '<td colspan="' + str(span) + '">' + col + '</td>'
            else:
                row += '<td>' + col + '</td>'
        row += '</tr>'
        table += row

    table += '</tbody></table>'
    return mark_safe(table)