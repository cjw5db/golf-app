from django.db import models
from django.urls import reverse_lazy
from django.core.validators import MaxValueValidator, MinValueValidator

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
    TEAM_SIZES = (
        (4, 'Four'),
        (6, 'Six'),
        (8, 'Eight'),
        (10, 'Ten'),
        (12, 'Twelve'),
    )

    name = models.CharField(max_length = 50, unique=True)
    teams = models.ManyToManyField('Team')
    rounds = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(1)])
    team_size = models.IntegerField(choices=TEAM_SIZES)

    def get_absolute_url(self):
        return reverse_lazy('golf:trip:detail', kwargs={'pk': self.pk})

    def __str__(self):
        """ String representation of object. """
        return self.name

class Group(models.Model):
    players = models.ManyToManyField('Player')
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE, null=True)
    round = models.IntegerField(null = True,validators=[MaxValueValidator(4), MinValueValidator(1)])
