from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Custom User Creation Form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Adding an email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Specify form fields
