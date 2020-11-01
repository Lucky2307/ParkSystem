from django import forms
from django.forms import ModelForm
from .models import complaintMessage
from django.utils.translation import gettext as _

class complaintMessageForm(ModelForm):
    class Meta:
        model = complaintMessage
        fields= ['member_id', 'name', 'phone_num', 'vehicle_number', 'complaint_message']
        widgets = {
            'complaint_message': forms.Textarea(attrs={"style": "resize:none"})
        }
        labels = {
            'member_id': _('Member ID'),
            'phone_num': _('Phone number')
        }