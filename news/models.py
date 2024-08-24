from django.db import models
from django.conf import settings
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title

class News(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="news")
    category = models.ManyToManyField(Category, related_name="news",default="1")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["created","updated"]

