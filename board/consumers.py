import json
from channels.generic.websocket import WebsocketConsumer
from models import Game

class ViewConsumer(WebsocketConsumer):
    def connect(self):
        #register the channel with the game_id
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        game = Game.objects.get(gameId=self.game_id)
        game.channel_name = self.channel_name
        game.save()
        self.accept()

    def disconnect(self, close_code):
        game = Game.objects.get(gameId=self.game_id)
        game.channel_name = ""
        game.save()
        pass

    #This function is to receive a message from the socket, which
    #shouldn't happen. Our socket is basically one way.
    def receive(self, text_data):
