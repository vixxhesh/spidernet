# userauth/forms.py

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username',
            'style': 'margin-bottom: 15px;'
        }),
        error_messages={
            'required': 'Please enter your username'
        },
        label='Username'
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password',
            'style': 'margin-bottom: 15px;'
        }),
        error_messages={
            'required': 'Please enter your password'
        }
    )
