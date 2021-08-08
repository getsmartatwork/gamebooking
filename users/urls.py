from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('register/',views.Registeration,name='register'),
   
    path('login/', views.login, name='login'),
    path('crud/', include(router.urls)),
]