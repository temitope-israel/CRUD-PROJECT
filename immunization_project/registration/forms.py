from django.core import validators
from django import forms
from .models import Registration
from django.forms.widgets import DateInput


class DateInput(forms.DateInput):
    input_type = 'date'

class ChildRegistration(forms.ModelForm):
    class Meta:
        model = Registration
        """child_dob = forms.DateField(widget=DatePickerInput(options={"format": "mm/dd/yyyy", "autoclose": True}))"""
        fields = ['child_name', 'child_age', 'child_dob', 'child_gender', 'mother_name', 'mother_age']
        
        widgets = {
            'child_dob': DateInput(attrs={'class': 'form-control'}),
            'child_name': forms.TextInput(attrs={'class': 'form-control'}),
            'child_age': forms.TextInput(attrs={'class': 'form-control'}),
            'child_gender': forms.Select(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_age': forms.TextInput(attrs={'class': 'form-control'}),
        }
       