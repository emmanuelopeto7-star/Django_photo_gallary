from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Extra information about a user, kept separate from Django's
    built-in User model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username
