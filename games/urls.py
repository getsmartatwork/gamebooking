from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()

router.register(r'hostgame',  views.HostGameViewSet)
router.register(r'schedule',  views.ScheduleViewSet)



urlpatterns = [
    path('crud/', include(router.urls)),
]