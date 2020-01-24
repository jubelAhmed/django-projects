from django import template
from django.template.defaultfilters import stringfilter

register = template.library()

@register.filter(name='cut')
def cut(value,arg):
    """ remove all values of arg from the given string"""
    return value.replace(arg,'')

@register.filter
@stringfilter
def low(value):
    return value.lower()


