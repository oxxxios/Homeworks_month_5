from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import DirectorListSerializer, MovieListSerializer, ReviewListSerializer, MoviesCreateSerializer, DirectorCreateSerializer, ReviewCreateSerializer
from .models import Movie, Director, Review
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieListSerializer(movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = MoviesCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'message':'data with errors', 'errors': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            movie = Movie.objects.create(
            title=request.data.get('title'),
            description=request.data.get('description'),
            duration=request.data.get('duration'),
            director_id=request.data.get('director_id')
        )
        movie.save()
        print(movie)
        return Response(status.HTTP_201_CREATED, data={'message':'Successfully created'})




@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def director_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        data = DirectorListSerializer(directors, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer =DirectorCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'message': 'data with errors', 'errors': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            director = Director.objects.create(
                name=request.data.get('name')
            )
            director.save()
            print(director)
            return Response(status.HTTP_201_CREATED, data={'message':'Successfully created'})



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewListSerializer(reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ReviewCreateSerializer(data=request.data)
        if not serializer.is_valid():
             return Response(data={'message': 'data with errors', 'errors': serializer.errors},
                                status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            review = Review.objects.create(
                text=request.data.get('text'),
                movie_id=request.data.get('movie_id'),
                stars=request.data.get('stars')
            )
            review.save()
            print(review)
            return Response(status.HTTP_201_CREATED, data={'message': 'Successfully created'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_reviews_view(request):

    reviews = Review.objects.all()

    data = ReviewListSerializer(reviews, many=True).data
    return Response(data=data)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def movie_item_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error':'movie not found'})
    if request.method == 'GET':
        serializer = MovieListSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data={'message': 'Successfully deleted'}, status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = MoviesCreateSerializer
        serializer.is_valid(raise_exception=True)
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data={'message':'successfully Updated', 'movie': MovieListSerializer(movie).data})




@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def director_item_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error':'director not found'})
    if request.method == 'GET':
        serializer = DirectorListSerializer(director)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
    else:
        serializer = DirectorCreateSerializer
        serializer.is_valid(raise_exception=True)
        director.name = request.data.get('name')
        director.save()
        return Response(data={'message':'Successfully Updated', 'director': DirectorListSerializer(director).data})


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_item_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error':'Product not found'})
    if request.method == 'GET':
        serializer = ReviewListSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
    else:
        serializer = ReviewCreateSerializer
        serializer.is_valid(raise_exception=True)
        review.text = request.data.get('text')
        review.movie_id = request.data.get('movie_id')
        review.stars = request.data.get('stars')
        review.save()
        return Response(data={'message': 'Successfully Updated', 'director': ReviewListSerializer(review).data})