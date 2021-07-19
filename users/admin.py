from django.contrib import admin

from .models import HostGame, profileModel,Team

# Register your models here.

admin.site.register(profileModel)

admin.site.register(HostGame)
admin.site.register(Team)

