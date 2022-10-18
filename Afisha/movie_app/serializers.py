from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class DirectorListSerializers(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = 'id name movies_count'.split()

    def get_movies_count(self, obj_director):
        return obj_director.movies.count()


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()


class MovieListSerializers(serializers.ModelSerializer):
    director = DirectorSerializers()

    class Meta:
        model = Movie
        fields = 'title description duration director director_name'.split()


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title'.split()


class ReviewListSerializers(serializers.ModelSerializer):
    movie = MovieSerializers()

    class Meta:
        model = Review
        fields = 'text movie movie_title stars'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id movie text stars'.split()

    def to_representation(self, instance):
        show = super().to_representation(instance)
        show['movie'] = instance.movie.title

        return show


class MoviesReviewsListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'title reviews rating'.split()

    def get_rating(self, obj_movie):
        sum_ = 0
        for i in obj_movie.reviews.all():
            sum_ += int(i.stars)
        return round(sum_ / obj_movie.reviews.count(), 1) if obj_movie.reviews.count() else "This movie has no rating"


class DirectorBaseValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=100, required=True)  # True - обязательное поле


class DirectorCreateSerializer(DirectorBaseValidateSerializer):
    def validate_name(self, name):
        if Director.objects.filter(name=name):
            raise ValidationError("Director's name must be unique")
        return name


class DirectorUpdateSerializer(DirectorBaseValidateSerializer):
    pass


class MovieBaseValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_null=True, allow_blank=True)
    duration = serializers.CharField(allow_blank=True, allow_null=True)
    director = serializers.IntegerField(min_value=1)


class MovieCreateSerializer(MovieBaseValidateSerializer):
    def validate_director(self, director):
        try:
            Director.objects.get(id=director)
        except Director.DoesNotExist:
            raise ValidationError(f'Director with id = {director} Not Found')
        return director


class MovieUpdateSerializer(MovieBaseValidateSerializer):
    pass


class ReviewBaseValidateSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    movie = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(default=0, min_value=0, max_value=5)


class ReviewCreateSerializer(ReviewBaseValidateSerializer):
    def validate_movie(self, movie):
        try:
            Movie.objects.get(id=movie)
        except Movie.DoesNotExist:
            raise ValidationError(f'Movie with id = {movie} Not Found')
        return movie


class ReviewUpdateSerializer(ReviewBaseValidateSerializer):
    pass
