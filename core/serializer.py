from .models import User, Problem
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProblemSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(write_only=True, required=False)
    photo_url = serializers.URLField(read_only=True, required=False)

    class Meta:
        model = Problem
        fields = ["description", "photo", "user", "photo_url", "id"]
