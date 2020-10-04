from django.urls import path

from . import views

urlpatterns = [
    #These are all gets->
    path('', views.index, name='index'),
    path('create', views.createGameControl, name='createGameControl'),
    path('control/<char:game_id>', views.getControl, name='getControl'),
    path('view', views.viewIndex, name='viewIndex'),
    path('view/create', views.createGameView, name='createGameView'),
    path('view/<char:game_id>', views.getView, name='getView'),
    #These are all posts (from the control.html page) ->
    path('team:<int:teamId>/name=<char:name>', views.setName, name='setName'),
    path('team:<int:teamId>/+<int:score>', views.addScore, name='addScore'),
    path('team:<int:teamId>/-<int:score>', views.subScore, name='subScore'),
    path('team:<int:teamId>/=<int:score>', views.setScore, name='setScore'),
    path('<int:game_id>/timer/+<int:seconds>', views.addTime, name='addTime'),
    path('<int:game_id>/timer/-<int:seconds>', views.subTime, name='subTime'),
    path('<int:game_id>/timer/=<int:seconds>', views.setTime, name='setTime'),
    path('<int:game_id>/quarter/+', views.addQuarter, name='addQuarter'),
    path('<int:game_id>/quarter/-', views.subQuarter, name='subQuarter'),
    path('<int:game_id>/quarter/=<int:quarter>', views.setQuarter, name='setQuarter'),
    path('<int:game_id>/quarter/+', views.addDown, name='addDown'),
    path('<int:game_id>/quarter/-', views.subDown, name='subDown'),
    path('<int:game_id>/down/=<int:down>', views.setDown, name='setDown'),
    path('<int:game_id>/end', views.endGame, name='endGame'),
    path('history/<int:number>', views.getHistory, name='getHistory'),
    path('activate/<int:game_id>', views.activate, name='activate'),
    path('<int:game_id>/setBlurb', views.setBlurb, name='setBlurb')
]
