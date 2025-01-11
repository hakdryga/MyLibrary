from django.db import models

CATEGORY_CHOICES = (
    ('python','PYTHON'),
    ('java', 'JAVA'),
    ('aws','AWS'),
    ('javascrit','JAVASCRIPT'),
    ('react','REACT'),
)
class Tutorial(models.Model):
    name = models.CharField(max_length=70)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='python')
    note = models.TextField()
