from django import template
from django.contrib.auth.models import User

register = template.Library()

"""
https://djangoproject.jp/doc/ja/1.0/howto/custom-template-tags.html
"""
@register.filter
def get_username(value):
    u = User.objects.get(id=value)
    return u.username