from django.shortcuts import render, redirect, get_object_or_404
from .forms import FilmForm, RatingForm, CustomUserCreationForm
from .models import Film, Rating
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm


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


def custom_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error_message = "Неверный адрес электронной почты или пароль."
                return render(request, 'login.html', {'login_form': login_form, 'error_message': error_message})
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})


def film_detail(request,film_id):
    film = get_object_or_404(Film, pk=film_id)
    return render(request,'film_detail.html',{'film':film})