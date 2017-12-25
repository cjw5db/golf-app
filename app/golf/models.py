from django.db import models
from django.urls import reverse_lazy

import os

class Player(models.Model):
    name = models.CharField(max_length=50, unique=True)
    handicap = models.IntegerField()
    team = models.ForeignKey('Team', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse_lazy('golf:player:detail', kwargs={'pk': self.pk})

    def __str__(self):
        """ String representation of object. """
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse_lazy('golf:teams:detail', kwargs={'pk': self.pk})

    def __str__(self):
        """ String representation of object. """
        return self.name

class Trip(models.Model):
    name = models.CharField(max_length = 50, unique=True)
    teams = models.ManyToManyField('Team')
    rounds = models.IntegerField()
    team_size = models.IntegerField()

    def get_absolute_url(self):
        return reverse_lazy('golf:trip:detail', kwargs={'pk': self.pk})

    def __str__(self):
        """ String representation of object. """
        return self.name
