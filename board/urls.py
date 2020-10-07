from django.urls import path

from . import views

urlpatterns = [
    #These are all gets->
    path('', views.index, name='index'),
    path('control/<char:game_id>', views.getControl, name='getControl'),
    path('view', views.viewIndex, name='viewIndex'),
    path('view/<char:game_id>', views.getView, name='getView'),
    #These are all posts (from the control.html page) ->
    path('<int:game_id>/<char:team>/+<int:score>', views.addScore, name='addScore'),
    path('<int:game_id>/<char:team>/-<int:score>', views.subScore, name='subScore'),
    path('<int:game_id>/<char:team>/=<int:score>', views.setScore, name='setScore'),
    path('<int:game_id>/<char:team>/<char:name>', views.setName, name='setName'),
    path('<int:game_id>/time/+<int:seconds>', views.addTime, name='addTime'),
    path('<int:game_id>/time/-<int:seconds>', views.subTime, name='subTime'),
    path('<int:game_id>/time/=<int:seconds>', views.setTime, name='setTime'),
    path('<int:game_id>/quarter/+<int:quarter>', views.addQuarter, name='addQuarter'),
    path('<int:game_id>/quarter/-<int:quarter>', views.subQuarter, name='subQuarter'),
    path('<int:game_id>/quarter/=<int:quarter>', views.setQuarter, name='setQuarter'),
    path('<int:game_id>/down/+<int:down>', views.addDown, name='addDown'),
    path('<int:game_id>/down/-<int:down>', views.subDown, name='subDown'),
    path('<int:game_id>/down/=<int:down>', views.setDown, name='setDown'),
    path('<int:game_id>/end', views.endGame, name='endGame'),
    path('<int:game_id>/possession=<char:team>', views.setPossession, name='setPossession'),
    path('<int:game_id>/setBlurb', views.setBlurb, name='setBlurb'),
    path('<int:game_id>/setTitle', views.setTitle, name='setTitle'),
]
