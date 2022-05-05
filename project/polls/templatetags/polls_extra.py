from atexit import register
from django import template
from polls.models import Categories
register = template.Library()

@register.simple_tag(name = 'getcats')
def get_catigories():
    return Categories.objects.all()