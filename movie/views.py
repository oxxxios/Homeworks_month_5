from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Director_list
from .serializers import Movie_list,Rewie_list
from .models import Director, Movie,Review



@api_view(['GET'])
def DirectorApiView(request):
    direcrors = Director.objects.all()
    data = Director_list(direcrors, many=True).data
    return Response(data=data)

@api_view(['GET'])
def MovieApiView(request):
    movie = Movie.objects.all()
    data = Movie_list(movie, many=True).data
    return Response(data=data)

@api_view(['GET'])
def ReviewApiView(request):
    movie = Review.objects.all()
    data = Movie_list(movie, many=True).data
    return Response(data=data)







