from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True, verbose_name="Avatar",
                               help_text="Upload avatar")

    def __str__(self):
        return self.username
