from django.shortcuts import render

from tutorials.models import Tutorial


def tutorials_list(request):
    tutorials = Tutorial.objects.all()
    return render(request, "tutorials.html", {"tutorials": tutorials})
