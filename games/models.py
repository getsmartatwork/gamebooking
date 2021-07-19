from django.db import models

# Create your models her
from django.conf import settings
from django.db import models
from django.utils import timezone

class Schedule(models.Model):
    hostgame=models.ForeignKey(HostGame, on_delete=models.CASCADE)
    profile_a=models.ForeignKey(profileModel, on_delete=models.CASCADE)
    profile_b=models.ForeignKey(Profile, on_delete=models.CASCADE)
    team_a=models.ForeignKey(Team, on_delete=models.CASCADE)
    team_b=models.ForeignKey(Team, on_delete=models.CASCADE)
    winner_player=models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    winner_Team=models.ForeignKey(Team, on_delete=models.CASCADE)
    created_date=models.DateTimeField(default=timezone.now)
    start_datetime=models.DateTimeField(default=timezone.now)
    end_datetime=models.DateTimeField(default=timezone.now)
    city=models.ForeignKey(City, on_delete=models.CASCADE)
    address=models.TextField(max_length=200)
    image=models.ImageField() 

    def __str__(self):
        return "{} {}".format(self.winner_player,self.winner_Team) 