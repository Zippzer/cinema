from django import forms
from .models import Film
from .models import Rating
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('title', 'description', 'img')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username',)


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['movie', 'value']
