from django.db import models


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Enterprise(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name