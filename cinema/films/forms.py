from django import forms
from .models import Film
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Rating


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('title', 'description', 'img')


class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class YourAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['movie','value']

