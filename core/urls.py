from django.contrib import admin
from django.urls import path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r"user", views.UserViewSet, basename="user")
router.register(r"problems", views.ProblemViewSet, basename="problem")
urlpatterns = router.urls
