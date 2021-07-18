from django.contrib import admin
from .models import profileModel,TeamMember

# Register your models here.

admin.site.register(profileModel)
admin.site.register(TeamMember)