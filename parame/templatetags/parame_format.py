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

    table = '<table class="table table-sm table-bordered table-hover">\n'
    table += '<thead class="thead-light"><th colspan="' + str(max_cols_count) +  '">Parameter Sheet</th><thead>\n'
    table += '<tbody>\n'
    for line in esc(value).splitlines():
        cols_count = len(line.split('|'))
        elm = []
        for col in line.split('|'):
            span = max_cols_count - cols_count + 1
            if span > 1:
                elm.append('<td colspan="' + str(span) + '">' + gen_div(col) + '</td>')
            else:
                elm.append('<td>' + gen_div(col) + '</td>')
        table += gen_row("".join(elm))

    table += '</tbody></table>'
    return mark_safe(table)

def gen_row(value):
    return '<tr>' + value + '</tr>\n'

def gen_div(value):
    import re

    sharps_count = 0
    for v in value:
        if v == '#':
            sharps_count += 1
        else:
            break
    if sharps_count > 0:
        return '<div class="ps' + str(sharps_count) + '">' + re.sub(r'^#+', '', value) + '</div>'
    else:
        return value