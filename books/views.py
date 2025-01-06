from django.shortcuts import render


def books_list(request):
    # user_name = request.GET.get("user_name") or "world"  # http://127.0.0.1:8000/books/?user_name=Ania
    # return HttpResponse("Hello, {}!".format(user_name))
    user_name = "ANIA"
    return render(request, "books.html", {"user_name": user_name})


def index(request):
    return render(request, "index.html")


def search_book(request):
    search = request.GET.get("search") or "world"
    return render(request, "search_book.html", {"search": search})
