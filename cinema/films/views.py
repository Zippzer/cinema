from django.shortcuts import render,redirect,get_object_or_404
from .forms import FilmForm,RatingForm
from .models import Film,Rating
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreation,YourAuthenticationForm
from django.contrib.auth import logout
from django.views import View

def index(request):
    movie=Film.objects.all()
    return render(request,'index.html',{'movie': movie})


def add_film(request):
    form = FilmForm()
    if request.method == 'POST':
        form = FilmForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = FilmForm()

    return render(request,'film_upload.html',{'form': form})


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreation()
        return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = YourAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signin.html', {'form': form})
    else:
        form = YourAuthenticationForm()
        return render(request, 'signin.html', {'form': form})


def logout_m(request):
    logout(request)
    return redirect('index')


def rate_movie(request,movie_id):
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

