from django.shortcuts import render

from .models import Game

def index(request):
    games = Game.objects.all
    return render(request, 'games/index.html', {'games': games})
