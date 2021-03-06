from django.shortcuts import get_object_or_404, render
from models import *
from channels.layers import get_channel_layer
from Init.py import get_or_create, get_view, get_timer_string
from django.http import JsonResponse

#################################################################################
#CONTROL - 'create/'  'control/<char:game_id>'
def index(request):
    #MAYBE SOMEDAY, BUT NOT TODAY.
    #Only display games that already have a channel_name.
    #This means the game was created from the view and it's waiting for a control.
    #active_games = Game.objects.order_by('-date').filter(channel_name!="")[:5]
    #context = {'games' : active_games}
    #return render(request, 'board/index.html', context)

    #CREATE OR RETURN THE CURRENT (AND ONLY) Game
    context = get_or_create_game()
    return render(request, 'board/control.html', context)

def getControl(request):
    #return the control.html page for the given game_id
    context = get_or_create_game(game_id)
    return render(request, 'board/control.html', context)

#################################################################################
#VIEWS - 'view'  'view/<char:game_id>'
def viewIndex(request):
    #MAYBE SOMEDAY BUT NOT TODAY
    #Display the already initialized games and give an option to create a new one.
    #active_games = Game.objects.order_by('-date').filter(active=True)[:15]
    #context = {'games' : active_games}
    #return render(request, 'board/viewIndex.html', context)

    #RETURN THE VIEW FOR THE SINGLE GAME
    context = get_game()
    return render(request, 'board/control.html', context)

def getView(request):
    #This is the function for getting the actual scoreboard view used by OBS.
    #This is always where the channel is initialized and tied to the game id.
    #It doesn't matter who created the game, once this function is
    #called (a game_id is required to be routed here), you can create the channel
    #and tie everything together using that id.

    #What should happen if someone accesses this url with an old/nonexistant game_id (route to viewIndex)
    context = get_game(game_id)
    return render(request, 'board/view.html', context)

#################################################################################
#NAME - 'team:<int:teamId>/name=<char:name>'
def setHomeName

def setName(request):
    game = Game.objects.get(game=game_id)
    if team == "home":
        game.homeTeam = name
    else:
        game.awayTeam = name
    game.save()
    return updateChannels(  Channels.objects, team + 'Team', name)

#################################################################################
#SCORE - 'team:<int:teamId>/=<int:score>'  'team:<int:teamId>/-<int:score>'
def addScore(request):
    game = Game.objects.get(game=game_id)
    runningScore = 0
    if team == "home":
        runningScore = game.homeScore + score
        game.homeScore = runningScore
    else:
        runningScore = game.awayScore + score
        game.awayScore = runningScore
    game.save()
    return updateChannels(  Channels.objects,
                    team + 'Score',
                    runningScore)

def subScore(request):
    game = Game.objects.get(game=game_id)
    runningScore = subSetValue(game.homeScore, score, 0)
    if team == "home":
        game.homeScore = runningScore
    else:
        game.awayScore = runningScore
    game.save()
    return updateChannels(  Channels.objects,
                    team + 'Score',
                    runningScore)

def setScore(request):
    game = Game.objects.get(game=game_id)
    runningScore = setInRange(score, 0, 150)
    if team == "home":
        game.homeScore = runningScore
    else:
        game.awayScore = runningScore
    game.save()
    return updateChannels(  Channels.objects,
                    team + 'Score',
                    runningScore)

#################################################################################
#TIME - '<int:game_id>/timer/=<int:time>'  '<int:game_id>/timer/-<int:seconds>'
def addTime(request):
    game = Game.objects.get(game_id=game_id)
    game.time = addSetValue(game.time, time, 900)
    game.save()
    return update_time(game.time)

def subTime(request):
    game = Game.objects.get(game_id=game_id)
    game.time = subSetValue(game.time, time, 0)
    game.save()
    return update_time(game.time)
    

def setTime(request):
    game = Game.objects.get(game_id=game_id)
    game.time = setInRange(time, 0, 900)
    game.save()
    return update_time(game.time)
    
def update_time(time):
    time_string = get_timer_string(time)
    return updateChannels( Channels.objects,
                    'time',
                    time_string)

#################################################################################
#QUARTER - '<int:game_id>/quarter/=<int:quarter>'  '<int:game_id>/quarter/+'
def addQuarter(request):
    game = Game.objects.get(game=game_id)
    game.quarter = addSetValue(game.quarter, 1, 4)
    game.save()
    return update_quarter(game.quarter)

def subQuarter(request):
    game = Game.objects.get(game=game_id)
    game.quarter = subSetValue(game.quarter, 1, 1)
    game.save()
    return update_quarter(game.quarter)

def setQuarter(request):
    game = Game.objects.get(game=game_id)
    game.quarter = setInRange(quarter, 1, 4)
    game.save()
    return update_quarter(game.quarter)
    
def update_quarter(quarter):
    return updateChannels(  Channels.objects,
                    'quarter',
                    quarter)

#################################################################################
#DOWN - '<int:game_id>/down/=<int:down>'  '<int:game_id>/quarter/+'
def addDown(request):
    game = Game.objects.get(game=game_id)
    game.down = addSetValue(game.down, 1, 4)
    game.save()
    return update_down(game.down)

def subDown(request):
    game = Game.objects.get(game=game_id)
    game.down = subSetValue(game.down, 1, 1)
    game.save()
    return update_down(game.down)

def setDown(request):
    game = Game.objects.get(game=game_id)
    game.down = setInRange(down, 1, 4)
    game.save()
    return update_down(game.down)
    
def update_down(down):
    return updateChannels(  Channels.objects,
                    'down',
                    down)

################################################################################
#ADMIN
def setBlurb(request):
    game = Game.objects.get(game=game_id)
    game.title = request.post['blurb']
    game.save()
    return updateChannels(  Channels.objects,
                    'blurb',
                    game.blurb)

def setTitle(request):
    game = Game.objects.get(game=game_id)
    game.title = request.post['title']
    game.save()
    return updateChannels(  Channels.objects,
                    'title',
                    game.title)

def setPossession(request):
    return HttpResponse("Set Possession.")

################################################################################
#UTILS
def subSetValue(runningValue, valueDelta, valueLowerThreshold):
    if runningValue - valueDelta <= valueLowerThreshold:
        return valueLowerThreshold
    else:
        return runningValue - valueDelta

def addSetValue(runningValue, valueDelta, valueUpperThreshold):
    if runningValue + valueDelta >= valueUpperThreshold:
        return valueUpperThreshold
    else:
        return runningValue + valueDelta

def setInRange(value, lowerThreshold, upperThreshold):
    if value <= upperThreshold:
        if value >= lowerThreshold:
            return value
        else:
            return lowerThreshold
    else:
        return upperThreshold

def updateChannels(channels, type, value):
    channel_layer = get_channel_layer()
    for channel in channels:
        await channel_layer.send(channel.channel_name, {
            "type": type,
            "data": value,
        })
    return JsonResponse({   "type": type,
                            "data": value})
