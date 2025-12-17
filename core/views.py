from rest_framework import response, status
from rest_framework import mixins, viewsets
from rest_framework import generics
from .models import User, Problem

from .serializer import UserSerializer, ProblemSerializer
from cloudinary.uploader import upload

# Create your views here.


class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class ProblemViewSet(
#     mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
# ):
#     queryset = Problem.objects.all()
#     serializer_class = ProblemSerializer

#     def create(self, request):
#         data = self.request.data
#         serializer = ProblemSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         photo_file = serializer.validated_data.pop("photo", None)
#         if photo_file:
#             url = upload(photo_file)
#             image_url = url["secure_url"]
#             serializer.save(photo_url=image_url)
#             return response.Response(serializer.data, status=status.HTTP_201_CREATED)
#         return response.Response(status=status.HTTP_400_BAD_REQUEST)


class ProblemViewSet(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

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
