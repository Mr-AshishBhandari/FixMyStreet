from django.contrib import admin
from django.urls import path

from rest_framework import routers

from . import views

urlpatterns = [
    path("user/", views.UserViewSet.as_view(), name="user"),
    path("problem/", views.ProblemViewSet.as_view(), name="problem"),
    path(
        "problem/<int:pk>", views.ProblemDetailViewSet.as_view(), name="detail_problem"
    ),
]
