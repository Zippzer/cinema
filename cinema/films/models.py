from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Film(models.Model):
    title=models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='images',default='path/to/default/image.jpg')


class User(AbstractUser):
    pass


class Rating(models.Model):
    movie = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(1)])

    class Meta:
        unique_together = ('movie', 'user')

