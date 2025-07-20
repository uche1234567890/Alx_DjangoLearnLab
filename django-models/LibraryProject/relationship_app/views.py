from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book

def list_books(request):
    books = Book.objects.select_related('author').all()

    if not books:
        return HttpResponse("No books found.")

    output = "Books in Database:\n"
    for book in books:
        output += f"- {book.title} by {book.author.name}\n"

    return HttpResponse(output, content_type="text/plain")
