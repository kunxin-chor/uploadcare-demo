from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=255, blank=False)
    photo = ImageField(null=True)
