from django.contrib import admin
from .models import HostGame, profileModel

# Register your models here.

admin.site.register(profileModel)
admin.site.register(HostGame)