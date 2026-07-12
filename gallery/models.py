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


class Tag(models.Model):
    """A single label, like 'portrait' or 'landscape', used to filter photos."""

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    """A photo, portrait, or artwork in the gallery."""

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    tags = models.ManyToManyField(Tag, blank=True, related_name='photos')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')
    created_at = models.DateTimeField(auto_now_add=True)

    liked_by = models.ManyToManyField(User, blank=True, related_name='liked_photos')
    disliked_by = models.ManyToManyField(User, blank=True, related_name='disliked_photos')

    def __str__(self):
        return self.title
