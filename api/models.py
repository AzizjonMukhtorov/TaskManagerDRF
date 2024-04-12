from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)


class Task(models.Model):
    title = models.CharField(max_length=50)
    create_at = models.DateTimeField()
    is_com = models.BooleanField()
    user = models.ForeignKey(CustomUser, related_name = 'tasks', on_delete=models.CASCADE)