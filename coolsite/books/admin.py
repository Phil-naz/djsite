from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin


class BooksAdmin(admin.ModelAdmin):   # TranslationAdmin
    list_display = ('name', 'author', 'get_html_photo')
    fields = ('name', 'author', 'author_description', 'photo')   # fields at page of each object
    list_display_links = ('author',)  # make links for editing
    search_fields = ('name', 'author')  # for searching in this columns
    list_editable = ('name',)   # function for edit data in admin panel
    list_filter = ('publishing_house',)


    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50")

    get_html_photo.short_description = "Миниатюра"


admin.site.register(Books, BooksAdmin)
