from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class Film(models.Model):
    title=models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    img = models.ImageField(upload_to='images',default='path/to/default/image.jpg')

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email


class Rating(models.Model):
    movie = models.ForeignKey(Film, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    value = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(1)])

    class Meta:
        unique_together = ('movie', 'user')

