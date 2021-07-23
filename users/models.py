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



class HostGame(models.Model):
    players_choices=(
        ("players","players"),
        ("teams","teams")
    )
    title=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField()
    game=models.ForeignKey(Game,on_delete=models.CASCADE)
    players_team=models.CharField(max_length=20,choices=players_choices)
    no_of_players=models.IntegerField()
    no_of_teams=models.IntegerField()
    no_of_players_in_team=models.IntegerField()
    created_date=models.DateTimeField(default=timezone.now)
    status=models.BooleanField(default=True)
    start_datetime=models.DateTimeField(default=timezone.now)
    end_date_time=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {}".format(self.created_date,self.status)

        return "{}".format(self.about)    
    

class Team(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField()
    created_date=models.DateTimeField(default=timezone.now)
    status=models.BooleanField(default=True)
    game=models.ForeignKey(Game,on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.title,self.game)  

class TeamMember(models.Model):
    team=models.ForeignKey(Team, on_delete=models.CASCADE)
    profile=models.ForeignKey(profileModel, on_delete=models.CASCADE)
    is_capatain=models.BooleanField()
    created_date=models.DateTimeField(default=timezone.now)
    status=models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(self.is_capatain, self.created_date, self.status)    

