from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from films.views import index,add_film,rate_movie,signup, custom_logout,custom_login,film_detail
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('upload/',add_film, name='upload'),
    path('signup/',signup,name='signup'),
    path('logout/',custom_logout, name='logout'),
    path('rate/<int:movie_id>/',rate_movie,name='rate_movie'),
    path('login/', custom_login, name='custom_login'),
    path('films/<int:film_id>/',film_detail,name='film_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
