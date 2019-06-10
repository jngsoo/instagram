from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    photo = ImageField(blank=True, manual_crop="")
    date = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField(null=True, max_length=500)

    class Meta():
        ordering = ['-date']
