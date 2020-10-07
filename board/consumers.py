import json
from channels.generic.websocket import WebsocketConsumer
from models import Channels

class ViewConsumer(WebsocketConsumer):
    def connect(self):
        #register the channel with the game_id
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        Channels.objects.create(game=game_id, channel_name = self.channel_name)
        #add a new channel row
        self.accept()

    def disconnect(self, close_code):
        #remove this channel from the table
        Channels.objects.filter(channel_name = self.channel_name).delete()

    #This function is to receive a message from the socket, which
    #shouldn't happen. Our socket is basically one way.
    def receive(self, text_data):
