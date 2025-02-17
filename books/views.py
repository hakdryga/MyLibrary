from django.shortcuts import render
from .models import Book


def books_list(request):
    books = Book.objects.all()
    return render(request, "books.html", {"books": books})


def index(request):
    return render(request, "index.html")


def search_book(request):
    search = request.GET.get("search") or "world"
    return render(request, "search_book.html", {"search": search})
