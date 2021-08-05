from django.shortcuts import render

# Create your views here.

from django.shortcuts import (render, redirect, get_object_or_404,HttpResponse, HttpResponseRedirect)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets




from rest_framework import permissions
from .serializers import  HostGameSerializer,ScheduleSerializer
from .models import HostGame,Schedule




class HostGameViewSet(viewsets.ModelViewSet):
    queryset = HostGame.objects.all()
    serializer_class = HostGameSerializer
    # permission_classes = [permissions.IsAuthenticated]




class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    # permission_classes = [permissions.IsAuthenticated]

    