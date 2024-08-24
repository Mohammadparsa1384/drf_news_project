from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    job = models.CharField(max_length=50)
    bio = models.TextField()