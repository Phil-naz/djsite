from django import template
from books.models import *


register = template.Library()



@register.simple_tag(name='book_list')
def book_list():
    return Books.objects.all()
