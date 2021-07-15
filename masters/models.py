from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Game(models.Model):
    name = models.TextField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    status = models.TextField()
    no_of_players = models.CharField(max_length=200)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return "{} . {}".format(self.title, self.text)
