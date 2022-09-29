from rest_framework import serializers
from .models import Director,Movie,Review


class Director_list(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = [
            "id",
            'name',
        ]

class Movie_list(serializers.ModelSerializer):
    director = serializers.StringRelatedField()
    class Meta:
        model = Movie
        fields = '__all__'

class Rewie_list(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = ["movie", "text"]
