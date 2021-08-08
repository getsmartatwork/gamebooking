from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.db.models import fields
from django.db.models.base import Model

from rest_framework import serializers
from .models import HostGame,Schedule

class HostGameSerializer(serializers.ModelSerializer):

    class Meta:
        model = HostGame
        # fields = ('id','title','descriprion','image','game','players_team','no_of_players','no_of_teams','no_of_players_in_team','created_date','status','start_datetime','end_date_time')
        fields = '__all__'
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        # fields = ('hostgame','profile_a','profile_b','team_a','team_b','winner_player','winner_Team','created_date','start_datetime','end_datetime','city','address','image')
        fields = '__all__'