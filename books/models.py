from django.db import models

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
    publication_year = models.IntegerField()
    publisher = models.CharField(max_length=30)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.title
