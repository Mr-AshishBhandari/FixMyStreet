from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)


class Problem(models.Model):

    problem_status = (
        ("Re", "Received"),
        ("O", "Open"),
        ("P", "In progess"),
        ("R", "Resolved"),
        ("C", "Closed"),
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    status = models.CharField(max_length=2, choices=problem_status, default="Re")
    photo_url = models.URLField()
