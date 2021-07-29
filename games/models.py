from django.db import models

# Create your models her
from django.conf import settings
from django.db import models
from django.utils import timezone
from masters.models import Game,City
from users.models import Profile,Team,TeamMember

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
     

class Schedule(models.Model):
    hostgame=models.ForeignKey(HostGame, on_delete=models.CASCADE)
    profile_a=models.ForeignKey(Profile, related_name="profile_a", on_delete=models.CASCADE)
    profile_b=models.ForeignKey(Profile, related_name="profile_b", on_delete=models.CASCADE)
    team_a=models.ForeignKey(Team,  related_name="team_a",  on_delete=models.CASCADE)
    team_b=models.ForeignKey(Team, related_name="team_b", on_delete=models.CASCADE)
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