from django import forms
from .models import *

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service_name', 'rate']
        labels = {
            'service_name': 'Service Name',
            'rate': 'Price (in ₹)',
        }
        widgets = {
            'service_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex. Eyebrow', 'autocomplete': 'off', 'autofocus': 'on', 'required': 'true' }),
            'rate': forms.NumberInput(attrs={'class': 'form-control', 'required': 'true', 'value': '0'}),
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['customer_name', 'contact', 'is_repeat_customer', 'serving_staff', 'services', 'transaction_cost']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'placeholder': 'Ex. Unknown/New'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0000000000'}),
            'is_repeat_customer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'serving_staff': forms.Select(attrs={'class': 'form-select', 'required': 'true'}),
            'services': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'transaction_cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex. 450', 'required': 'true'}),
        }

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'contact', 'salary']
        labels = {
            'name': 'Staff Name',
            'contact': 'Contact Number',
            'salary': 'Salary',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter staff name', 'autocomplete': 'off', 'autofocus': 'on', 'value': '', 'required': 'true'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number', 'min': '7000000000', 'max': '9999999999'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter salary', 'min': '1000',}),
        }