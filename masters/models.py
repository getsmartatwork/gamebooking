from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Game(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    created_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)
    no_of_players = models.IntegerField(default=1)

    def __str__(self):
        return "{}".format(self.name)

class City(models.Model):
    
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    status=models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return "{} {}".format(self.created_date, self.status)