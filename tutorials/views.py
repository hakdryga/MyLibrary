from django.shortcuts import render


def tutorials_list(request):
    return render(request, "tutorials.html")
