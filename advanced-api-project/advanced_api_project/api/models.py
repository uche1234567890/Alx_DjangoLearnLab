from django.db import models
from datetime import datetime

class Author(models.Model):
    """
    Stores information about a book author.
    One Author can have many Books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Stores information about a book.
    Linked to an Author via a ForeignKey.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'  # Enables author.books to access related books
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"