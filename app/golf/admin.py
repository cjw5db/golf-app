from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	pass

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
	pass

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
	pass
