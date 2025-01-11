from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=50,
                            help_text="The name of the game")
    url = models.URLField(help_text="Game url")
    note = models.TextField(blank=True)
