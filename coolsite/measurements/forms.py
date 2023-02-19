from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class AddMeasurements(forms.ModelForm):
    class Meta:  # this class for formatting view of fields
        model = Measurements
        fields = ['Shoulders', 'Chest', 'Waist', 'Buttocks', 'Hips', 'Weight']
        widgets = {  # this is for individual design fields
            'Shoulders': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Chest': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Waist': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Buttocks': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Hips': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': True, 'type': 'number',}),
            'Weight': forms.NumberInput(attrs={'minlength': 2, 'maxlength': 3, 'required': None, 'type': 'number',}),
        }