from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Books)
class BooksTranslationOptions(TranslationOptions):
   fields = ('name', 'author', 'author_description')

