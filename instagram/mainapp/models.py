from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Post(models.Model):
    pub_date = models.DateTimeField('date published!!', blank=True, null=True)
    content = models.TextField(blank=True)
    photo = ImageField(blank=True, manual_crop="")

    def __str__(self):
        return self.content