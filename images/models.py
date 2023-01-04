from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    img = models.ImageField(upload_to="img")
    # if user is deleted, images are deleted
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"id={self.id}"
    
