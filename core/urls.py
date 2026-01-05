from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("user/", views.UserViewSet.as_view(), name="user"),
    path("register/", views.UserRegisterViewSet.as_view(), name="user"),
    path("problem/", views.ProblemViewSet.as_view(), name="problem"),
    path(
        "problem_update/", views.ProblemUpdateViewSet.as_view(), name="update_problem"
    ),
    path(
        "problem/<int:pk>", views.ProblemDetailViewSet.as_view(), name="detail_problem"
    ),
]
