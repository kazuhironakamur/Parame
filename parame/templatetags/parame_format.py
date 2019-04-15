from django import template

register = template.Library()

def cut(value, arg):
    "入力から arg の値を全て取り去る"
    return value.replace(arg, '')