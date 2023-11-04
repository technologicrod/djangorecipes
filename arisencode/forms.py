from django import forms
from .models import *
from django.core.exceptions import ValidationError


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'password', 'account_type']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'instructions']

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['email', 'password']