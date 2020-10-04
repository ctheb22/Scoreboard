from django.db import models

# Create your models here.
class Event(models.Model):
    eventText = models.CharField(max_length=200)
    time = models.DateTimeField('time')

class Team(models.Model):
    teamId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Game(models.Model):
    gameId = models.AutoField(primary_key=True)
    homeTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    awayTeam = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    date = models.DateTimeField('date')
    active = models.BooleanField(default=True)
    blurb = models.TextField(default='')
    channel_name = models.CharField(max_length=200)
    

class Score(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    runningScore = models.IntegerField()

class GameState(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    timer = models.DurationField()
    quarter = models.IntegerField()
    down = models.IntegerField()
    date = models.DateTimeField('date')
