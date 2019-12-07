import os

from django import template


register = template.Library()

@register.filter
def filename(value):
    base = os.path.basename(value.file.name)
    return os.path.splitext(base)[0]