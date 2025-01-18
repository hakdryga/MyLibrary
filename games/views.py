from django.shortcuts import render
from .models import Game


def games_list(request):
    games = Game.objects.all()
    return render(request, "games.html", {"games": games})


def search_game(request):
    search = request.GET.get("search") or "world"
    return render(request, "search_game.html", {"search": search})
