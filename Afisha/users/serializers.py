from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise ValidationError('User already exist!')
        return username


class UserLoginValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
