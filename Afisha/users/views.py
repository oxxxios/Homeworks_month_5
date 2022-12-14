from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserLoginValidateSerializer, UserCreateSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user is not None:
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={'key': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# def register(request):
#     # username = request.data.get('username')
#     # password = request.data.get('password')
#     # User.objects.create_user(username=username, password=password)
#     serializer = UserCreateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     User.objects.create_user(**serializer.validated_data)
#     return Response(status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def login(request):
#     # username = request.data.get('username')
#     # password = request.data.get('password')
#     # user = authenticate(username=username, password=password)
#     serializer = UserLoginValidateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = authenticate(**serializer.validated_data)
#     if user is not None:
#         Token.objects.filter(user=user).delete()
#         token = Token. objects.create(user=user)
#         return Response(data={'key': token.key})
#     return Response(status=status.HTTP_401_UNAUTHORIZED)
