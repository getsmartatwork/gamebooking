from django.contrib import admin
from .models import Team, profileModel

# Register your models here.

admin.site.register(profileModel)
admin.site.register(Team)