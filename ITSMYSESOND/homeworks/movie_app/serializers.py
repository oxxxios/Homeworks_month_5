from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name '.split()


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration'.split()


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id  movie_name text stars '.split()


class MoviesBaseValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=3, max_length=100)
    description = serializers.CharField(required=False)
    duration = serializers.CharField(default='1:00')
    director = serializers.IntegerField(min_value=1)

    def validate_director(self, id):
        try:
            Director.objects.get(id=id)
        except Director.DoesNotExist:
            raise ValidationError(f'Director with id={id} Not Found')
        return id


class MoviesCreateSerializer(MoviesBaseValidateSerializer):
    def validate_title(self, title):
        if Movie.objects.filter(title=title):
            raise ValidationError('Title must be unic')
        return title


class MovieUpdateSerializer(MoviesBaseValidateSerializer):
    pass


class DirectorBaseValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1,max_length=255)


class DirectorCreateSerializer(DirectorBaseValidateSerializer):
    def validate_name(self, name):
        if Director.objects.filter(name=name):
            raise ValidationError('Name of Director must be unic')
        return name


class DirectorUpdateSerializer(DirectorBaseValidateSerializer):
    pass


class ReviewBaseValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=10, max_length=255)
    movie = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)

    def validate_movie(self, movie):
        try:
            Movie.objects.get(id=movie)
        except Movie.DoesNotExist:
            raise ValidationError(f'Movie with id={movie} Not Found')
        return movie


class ReviewCreateSerializer(ReviewBaseValidateSerializer):
    pass


class ReviewUpdateSerializer(ReviewBaseValidateSerializer):
    pass
