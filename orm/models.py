from django.db import models


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

