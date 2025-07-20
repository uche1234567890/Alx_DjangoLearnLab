from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library  # ✅ Required explicit import for validation

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()  # ✅ Explicit Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-Based View: Display library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_queryset(self):
        return Library.objects.prefetch_related("books").all()
