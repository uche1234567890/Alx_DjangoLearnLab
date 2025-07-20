from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-Based View: List all books with explicit Book.objects.all()
def list_books(request):
    books = Book.objects.all()  # ✅ Explicitly calling Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-Based View: Show a library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_queryset(self):
        # Preload books related to the library for performance
        return Library.objects.prefetch_related("books").all()
