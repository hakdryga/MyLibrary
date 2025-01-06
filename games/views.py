from django.shortcuts import render


def games_list(request):
    return render(request, "games.html")


def search_game(request):
    search = request.GET.get("search") or "world"
    return render(request, "search_game.html", {"search": search})
