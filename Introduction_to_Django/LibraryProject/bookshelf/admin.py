from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')     # Shows these columns in the list view
    list_filter = ('publication_year', 'author')               # Adds filter sidebar for these fields
    search_fields = ('title', 'author')                        # Enables search by title or author
