from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default="profile_pic.jpg")
