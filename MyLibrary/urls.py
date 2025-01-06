"""
URL configuration for MyLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import games.views
import tutorials.views
import books.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books.views.books_list),
    path('tutorials/', tutorials.views.tutorials_list),
    path('games/', games.views.games_list),
    path('', books.views.index),
    path('searchbook/', books.views.search_book),
    path('searchgame/', games.views.search_game)
]
