from django import template

register = template.Library()

from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

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

    table = '<table class="table table-sm table-bordered table-hover">'
    table += '<thead class="thead-light"><th colspan="' + str(max_cols_count) +  '">Parameter Sheet</th><thead>'
    table += '<tbody>'
    for line in esc(value).splitlines():
        cols_count = len(line.split('|'))
        elm = []
        for col in line.split('|'):
            span = max_cols_count - cols_count + 1
            if span > 1:
                elm.append('<td colspan="' + str(span) + '">' + col + '</td>')
            else:
                elm.append('<td>' + col + '</td>')
        table += gen_row("".join(elm))

    table += '</tbody></table>'
    return mark_safe(table)

def gen_row(value):
    return '<tr>' + value + '</tr>'