from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model
from cloudinary.uploader import upload

from .models import Problem
from .serializer import UserSerializer, ProblemSerializer
from .permissions import UpdateByAdminOnly

# Create your views here.


class UserViewSet(generics.ListCreateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserRegisterViewSet(generics.CreateAPIView):
    serializer_class = UserSerializer


class ProblemViewSet(generics.ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        photo_file = serializer.validated_data.pop("photo", None)
        user = self.request.user
        if photo_file:
            url = upload(photo_file)
            image_url = url["secure_url"]
            serializer.save(photo_url=image_url, user=user)
        else:
            print("Error occured")


class ProblemUpdateViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [UpdateByAdminOnly]


class ProblemDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    lookup_field = "pk"
    permission_classes = [IsAuthenticated]
