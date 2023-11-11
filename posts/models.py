from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=10000)
    date = models.DateTimeField()
    thumb = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.Title} ({self.date})'

# Create your models here.
