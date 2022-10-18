from django.contrib import admin
from .models import Director, Movie, Review

# Register your models here.

admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Review)
