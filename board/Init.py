from models import Game

def get_or_create_game(game_id):
    if(Game.objects.get(gameId=game_id).exists())
        game = Game.objects.get(gameId=game_id)
        context = {'game' : game,
                   'time' : get_timer_string(game.time)}
    else:
        game = Game.objects.create()
        context = {'game' : game,
                   'time' : get_timer_string(game.time)}
    return context

def get_game(game_id):
    game = Game.objects.get(gameId=game_id)
    return context = {'game' : game,
                      'time' : get_timer_string(game.time)}

def get_game():
    game = Game.objects[0]
    return context = {'game' : game,
                      'time' : get_timer_string(game.time)}

def get_timer_string(timer):
    remainder_seconds = timer % 60
    minutes = (timer - remainder_seconds) / 60
    return str(minutes) + ":" + str(remainder_seconds)
