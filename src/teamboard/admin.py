from django.contrib import admin
from teamboard.models import Team, Profile


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'score', 'not_banned']
    list_filter = ['score']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'team']
