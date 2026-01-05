from .models import  Problem
from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password"]


class ProblemSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(write_only=True, required=False)
    photo_url = serializers.URLField(read_only=True, required=False)

    class Meta:
        model = Problem
        fields = ["description", "photo", "user", "photo_url", "id"]
