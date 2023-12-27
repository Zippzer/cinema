from django.urls import path
from . import views
from .views import signup,rate_movie
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/',views.add_film, name='upload'),
    path('signup/', views.signup, name='signup'),
    path('rate/<int:movie_id>/',views.rate_movie,name='rate_movie')

]