from django.shortcuts import get_object_or_404, render
from models import *
from channels.layers import get_channel_layer

#################################################################################
#CONTROL - 'create/'  'control/<char:game_id>'
def index(request):
    active_games = Game.objects.order_by('-date').filter(active=True)[:15]
    context = {'games' : active_games}
    return render(request, 'board/index.html', context)

def createGameControl(request):
    #Initialize the model for a new game.
    #route to control.html for the created game.
    return HttpResponse("Created Game from Control.")

def getControl(request):
    #return the control.html page for the given game_id
    return HttpResponse("Got Control.")

#################################################################################
#VIEWS - 'view'  'view/<char:game_id>'
def viewIndex(request):
    #Display the already initialized games and give an option to create a new one.
    active_games = Game.objects.order_by('-date').filter(active=True)[:15]
    context = {'games' : active_games}
    return render(request, 'board/viewIndex.html', context)

def createGameView(request):
    #This is the function to create a game and view if OBS is started first.
    #Should initialize the game and view, making it findable from the index for the
    #game's control.html
    return HttpResponse("Created Game from View.")

def getView(request):
    #This is the function for getting the actual scoreboard view used by OBS.
    #This is always where the channel is initialized and tied to the game id.
    #It doesn't matter who created the game, once this function is
    #called (a game_id is required to be routed here), you can create the channel
    #and tie everything together using that id.

    #What should happen if someone accesses this url with an old/nonexistant game_id (route to viewIndex)
    return HttpResponse("Got View.")

#################################################################################
#NAME - 'team:<int:teamId>/name=<char:name>'
def setName(request):
    team = get_object_or_404(Team, pk=teamId)
    team.name = name
    team.save()
    game = Game.objects.get(home_team_id == teamId || away_team_id == teamId)
    #Assumes we can find the game.
    if game.home_team.teamId == teamId:
        updateChannel(  game.channel_name, 'home_team', team.name)
    else:
        updateChannel(  game.channel_name, 'away_team', team.name)
    #Update the Channel
    return HttpResponse("Set Team name.")

#################################################################################
#SCORE - 'team:<int:teamId>/=<int:score>'  'team:<int:teamId>/-<int:score>'
def addScore(request):
    scoreObject = Score.objects.get(team=teamId)
    scoreObject.runningScore += score
    scoreObject.save()
    updateChannel(  Game.objects.get(home_team == teamId || away_team == teamId).channel_name,
                    'score',
                    scoreObject.runningScore)
    #Update the Channel
    return HttpResponse("Added Score.")

def subScore(request):
    scoreObject = Score.objects.get(team=teamId)
    scoreObject.runningScore = subSetValue(scoreObject.runningScore, score, 0)
    scoreObject.save()
    updateChannel(  Game.objects.get(home_team == teamId || away_team == teamId).channel_name,
                    'score',
                    scoreObject.runningScore)
    #Update the Channel
    return HttpResponse("Subbed Score.")

def setScore(request):
    scoreObject = Score.objects.get(team=teamId)
    scoreObject.runningScore = setInRange(score, 0, 150)
    scoreObject.save()
    updateChannel(  Game.objects.get(home_team == teamId || away_team == teamId).channel_name,
                    'score',
                    scoreObject.runningScore)
    #Update the Channel
    return HttpResponse("Set Score.")

#################################################################################
#TIME - '<int:game_id>/timer/=<int:time>'  '<int:game_id>/timer/-<int:seconds>'
def addTime(request):
    stateObject = GameState.objects.filter(game_id=game_id)
    #stateObject.timer = addSetValue(stateObject.timer, seconds, 0)
    #Update the Channel
    return HttpResponse("Added Time.")

def subTime(request):
    stateObject = GameState.objects.filter(game_id=game_id)
    #stateObject.timer = subSetValue(stateObject.timer, seconds, 0)
    #Update the Channel
    return HttpResponse("Subbed Time.")

def setTime(request):
    stateObject = GameState.objects.filter(game_id=game_id)
    #stateObject.timer = time
    #Update the Channel
    return HttpResponse("Set Time.")

#################################################################################
#QUARTER - '<int:game_id>/quarter/=<int:quarter>'  '<int:game_id>/quarter/+'
def addQuarter(request):
    stateObject = GameState.objects.get(game=game_id)
    stateObject.quarter = addSetValue(stateObject.quarter, 1, 4)
    stateObject.save()
    updateChannel(  Game.objects.get(gameId=game_id).channel_name,
                    'quarter',
                    stateObject.quarter)
    #Update the Channel
    return HttpResponse("Added Quarter.")

def subQuarter(request):
    stateObject = GameState.objects.filter(game=game_id)
    stateObject.quarter = subSetValue(stateObject.quarter, 1, 1)
    stateObject.save()
    updateChannel(  Game.objects.get(gameId=game_id).channel_name,
                    'quarter',
                    stateObject.quarter)
    #Update the Channel
    return HttpResponse("Subbed Quarter.")

def setQuarter(request):
    stateObject = GameState.objects.filter(game=game_id)
    stateObject.quarter = setInRange(quarter, 1, 4)
    stateObject.save()
    updateChannel(  Game.objects.get(gameId=game_id).channel_name,
                    'quarter',
                    stateObject.quarter)
    #Update the Channel
    return HttpResponse("Set Quarter.")

#################################################################################
#DOWN - '<int:game_id>/down/=<int:down>'  '<int:game_id>/quarter/+'
def addDown(request):
    stateObject = GameState.objects.filter(game=game_id)
    stateObject.down = addSetValue(stateObject.down, 1, 4)
    stateObject.save()
    updateChannel(  Game.objects.get(gameId=game_id).channel_name,
                    'down',
                    stateObject.down)
    #Update the Channel
    return HttpResponse("Added Down.")

def subDown(request):
    stateObject = GameState.objects.filter(game=game_id)
    stateObject.down = subSetValue(stateObject.down, 1, 1)
    stateObject.save()
    updateChannel(  Game.objects.get(gameId=game_id).channel_name,
                    'down',
                    stateObject.down)
    #Update the Channel
    return HttpResponse("Subbed Down.")

def setDown(request):
    stateObject = GameState.objects.filter(game=game_id)
    stateObject.down = setInRange(down, 1, 4)
    stateObject.save()
    updateChannel(  Game.objects.get(gameId=game_id).channel_name,
                    'down',
                    stateObject.down)
    #Update the Channel
    return HttpResponse("Set Down.")

################################################################################
#ADMIN
def endGame(request):
    return HttpResponse("Ended Game.")

def getInactive(request):
    return HttpResponse("Got Inactive.")

def activate(request):
    return HttpResponse("Activated Game.")

def setBlurb(request):
    return HttpResponse("Set Blurb.")

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

def updateChannel(channel_name, type, value):
    channel_layer = get_channel_layer()
    await channel_layer.send(channel_name, {
        "type": type,
        "data": value,
    })
