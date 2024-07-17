from django.db import models
from django.contrib.auth.models import User
import datetime
from orm.models import Client

# Create your models here.


class Order(models.Model):
    ORDER_CHOICES = [
        ('wegiel', 'Węgiel'),
        ('koks', 'Koks'),
        ('biomasa', 'Biomasa'),
    ]

    badany_obiekt = models.CharField(max_length=10, choices=ORDER_CHOICES)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    opis = models.TextField()
    date = models.DateField(default=datetime.date.today, null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.badany_obiekt}'
