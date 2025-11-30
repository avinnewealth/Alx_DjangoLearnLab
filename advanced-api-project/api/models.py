from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Author model: stores the author’s name
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model: stores the book's title, publication year, and linked author
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',  # allows reverse lookup: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
