from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from cloudinary.uploader import upload

from .models import User, Problem
from .serializer import UserSerializer, ProblemSerializer
from .permissions import UpdateByAdminOnly

# Create your views here.


class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProblemViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [UpdateByAdminOnly]

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        photo_file = serializer.validated_data.pop("photo", None)

        if photo_file:
            url = upload(photo_file)
            image_url = url["secure_url"]
            serializer.save(photo_url=image_url)


class ProblemDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    lookup_field = "pk"
    permission_classes = [IsAuthenticated]
