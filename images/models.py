from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Image(models.Model):
    image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
