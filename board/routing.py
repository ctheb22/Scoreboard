from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/view/(?P<game_id>\w+)/$', consumers.ViewConsumer),
]
