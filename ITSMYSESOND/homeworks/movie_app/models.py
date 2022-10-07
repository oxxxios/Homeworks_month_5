from django.db import models
from django.db.models import Avg
# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name



class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete = models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(default=0, choices=RATE_CHOICES)

    @property
    def movie_name(self):
        try:
            return self.movie.title
        except:
            return ''

