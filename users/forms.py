from django import forms
import django
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
    
class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']

