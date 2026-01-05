from django.db import models
from django.conf import settings

# Create your models here.


class Problem(models.Model):

    problem_status = (
        ("Re", "Received"),
        ("O", "Open"),
        ("P", "In progess"),
        ("R", "Resolved"),
        ("C", "Closed"),
    )
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    status = models.CharField(max_length=2, choices=problem_status, default="Re")
    photo_url = models.URLField()
