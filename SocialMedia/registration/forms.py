from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import ProfileImage

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=40, required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    profile_pic = forms.ImageField(required=False)