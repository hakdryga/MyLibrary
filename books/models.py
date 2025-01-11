import datetime

from django.db import models
import datetime

CATEGORY_CHOICES = (
    ('it', 'IT'),
    ('travel', 'TRAVEL'),
    ('history', 'HISTORY'),
    ('languages', 'LANGUAGES'),
    ('kitchen', 'KITCHEN'),
)


class Book(models.Model):
    title = models.CharField(max_length=50,
                             help_text="Book's title")
    pages = models.IntegerField()
    author = models.CharField(max_length=20)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='kitchen')
    publication_date = models.DateField(
        verbose_name="Date the book was published.", default=datetime.date.today)
    note = models.TextField(blank=True)
