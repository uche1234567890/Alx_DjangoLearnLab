import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author_name = "Chinua Achebe"
try:
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with the name '{author_name}'.")

print("\n" + "="*40 + "\n")

# Query 2: List all books in a specific library
library_name = "National Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library.name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with the name '{library_name}'.")

print("\n" + "="*40 + "\n")

# Query 3: Retrieve the librarian for a specific library (using library=)
try:
    library = Library.objects.get(name=library_name)  # Get Library object first
    librarian = Librarian.objects.get(library=library)  # Use library=
    print(f"Librarian for {library.name}: {librarian.name}")
except (Library.DoesNotExist, Librarian.DoesNotExist):
    print(f"Librarian not found for '{library_name}'.")
