from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from masters.models import Game
# Create your models here.

from django.utils import timezone


class profileModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(blank=True,null=True)
    mobile_no=models.CharField(max_length=20)
    games_interest=models.ManyToManyField(Game)
    experience=models.TextField()
    about=models.TextField()
    status=models.BooleanField(default=True)
    created_date=models.DateTimeField(default=timezone.now)



    def __str__(self):
        return "{}".format(self.about)    

    
class TeamMember(models.Model):
    is_capatain=models.BooleanField()
    created_date=models.DateTimeField(default=timezone.now)
    status=models.BooleanField(default=True)

def __str__(self):
    return "{}".format(self.is_capatain,self.created_date,self.status)    
