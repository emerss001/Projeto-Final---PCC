from django.db import models
from django.contrib.auth.models import User


class account(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=25)
    