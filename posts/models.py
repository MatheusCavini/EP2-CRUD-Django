from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=10000)
    date = models.DateTimeField()
    thumb = models.CharField(max_length=255, blank=True)
    text1 = models.CharField(max_length=1000, blank=True)
    text2 = models.CharField(max_length=1000, blank=True)
    img2 = models.CharField(max_length=255, blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.title} ({self.date})'
    
class Comment(models.Model):
    date = models.DateTimeField()
    text = models.CharField(max_length=1000)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    project = models.ForeignKey(Post, on_delete=models.CASCADE)

