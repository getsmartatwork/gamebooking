from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class City(models.Model):
    city = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return "{} {}".format(self.city,self.created_date, self.status)