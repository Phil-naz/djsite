from django import forms
from .models import *
from django.core.exceptions import ValidationError


class AddBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): # it is for "ВЫБРАТЬ" instead of "---"
        super().__init__(*args, **kwargs)
        self.fields['publishing_house'].empty_label = "CHANGE | ВЫБРАТЬ"

    class Meta:  # this class for formatting view of fields
        model = Books
        fields = ['name_en', 'name_ru',  'author_en', 'author_ru', 'photo', 'author_description_en', 'author_description_ru', 'publishing_house']
        widgets = {  # this is for individual design fields
            'name_en': forms.TextInput(attrs={'class': 'form-input'}),
            'name_ru': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'author': forms.TextInput(attrs={'class': 'form-input'}),
            'author_description': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
        }

    def clean_name(self):  # for validation field. In name after _ field name
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return name