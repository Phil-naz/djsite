from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext as _


#     A Custom form for creating new users.
class UserAdminCreationForm(UserCreationForm):
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required=False, label=_('Phone number'))
    class Meta:
        model = get_user_model()
        fields = ['email', 'phone', 'first_name', 'last_name']
