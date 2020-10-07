from django.db import models

# Create your models here.
class Channels(models.Model):
    game = models.ForeignKey(on_delete=models.CASCADE)
    channel_name = models.char(max_length=200)

class Game(models.Model):
    gameId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default="The Game")
    homeTeam = models.CharField(max_length=200, default="Home")
    homeScore = models.IntegerField(default=0)
    awayTeam = models.CharField(max_length=200, default="Away")
    awayScore = models.IntegerField(default=0)
    date = models.DateTimeField('date')
    blurb = models.TextField(default='')
    time = models.int(default=900)
    possession = models.CharField(max_length=4, default="home")
    quarter = models.IntegerField(default=1)
    down = models.IntegerField(default=1)
