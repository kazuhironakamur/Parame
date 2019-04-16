from django import template

register = template.Library()

from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

"""
https://djangoproject.jp/doc/ja/1.0/howto/custom-template-tags.html
"""
@register.filter
def tab(value):

    max_col_count = confirm_max_col(value)

    table = '<table class="table table-sm table-bordered table-hover">\n'
    table += '<thead class="thead-light"><th colspan="' + str(max_col_count) +  '">Parameter Sheet</th><thead>\n'
    table += '<tbody>\n'
    for line in value.splitlines():
        table += parse_row(line, max_col_count)

    table += '</tbody></table>'
    return mark_safe(table)

def confirm_max_col(value):
    max_col_count = 0
    for line in value.splitlines():
        cols_count = len(line.split('|'))
        if max_col_count < cols_count:
            max_col_count = cols_count
    return max_col_count

def confirm_sharp_count(line):
    sharp_count = 0
    for v in line:
        if v == '#':
            sharp_count += 1
        else:
            break
    return sharp_count

def parse_row(line, max_col_count):
    import re

    esc = conditional_escape
    
    sharp_count = confirm_sharp_count(line)
    line = re.sub(r'^#+', '', line)
    
    split_line = line.split('|')
    cols_count = len(split_line)
    pan = max_col_count - cols_count + 1
    
    elm = []
    for col in split_line:
        
        if sharp_count > 0 and pan > 1:
            elm.append('<td colspan="' + str(pan) + '" class="ps' + str(sharp_count) + '">')
        elif pan > 1:
            elm.append('<td colspan="' + str(pan) + '">')
        elif sharp_count > 0:
            elm.append('<td class="ps' + str(sharp_count) + '">')
        else:
            elm.append('<td>')
            
        sharp_count = pan = 0
        elm.append(esc(col))
        elm.append('</td>')
    
    return '<tr>' + "".join(elm) + '</tr>\n'