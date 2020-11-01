from django import forms
from django.forms import ModelForm, MultiWidget
from .models import member
from django.utils.translation import gettext as _

class signupForm(ModelForm):
    class Meta:
        model = member
        fields= ['name', 'email', 'dob', 'phone_num', 'address']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={"style": "resize:none"})
        }
        labels = {
            'dob': _('Date of Birth'),
            'phone_num': _('Phone number')
        }