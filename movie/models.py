from django.db import models
from django.db.models import Model


class Director(models.Model):
    name = models.CharField(max_length=225)


    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    des =  models.CharField(max_length=250)
    dur = models.DurationField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



class Review(models.Model):
    rate = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    text = models.TextField("Ваш отзыв")
    movie = models.ForeignKey(to=Movie, verbose_name='Отзыв к фильму',
                              related_name='reviews', on_delete=models.CASCADE,
                              null=True, blank=True)
    stars = models.IntegerField(default=1, choices=rate)
