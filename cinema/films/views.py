from django.shortcuts import render, redirect, get_object_or_404
from .forms import FilmForm, RatingForm, CustomUserCreationForm
from .models import Film, Rating
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.views import View


def index(request):
    movie = Film.objects.all()
    return render(request, 'index.html', {'movie': movie})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})


def add_film(request):
    form = FilmForm()
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = FilmForm()

    return render(request, 'film_upload.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('/')


def rate_movie(request, movie_id):
    movie = get_object_or_404(Film, id=movie_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.movie = movie
            rating.user = request.user
            rating.save()
            return redirect('index')
    else:
        form = RatingForm()

    return render(request, 'rate_movie.html', {'form': form, 'movie': movie})
