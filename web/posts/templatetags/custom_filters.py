from django import template

register = template.Library()

@register.filter
def sub(value,argument):
    return value-argument