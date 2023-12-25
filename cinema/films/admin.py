from django.contrib import admin
from .models import User
from .models import Film


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass