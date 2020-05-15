from django.db import models


class GameData(models.Model):
	season_end_year = models.PositiveIntegerField()
	date = models.DateField()
	win = models.BooleanField()
	home = models.BooleanField()
	oppt = models.CharField(max_length=3)
	points_for = models.PositiveIntegerField()
	points_against = models.PositiveIntegerField()
	top_scorer = models.CharField(max_length=30)
