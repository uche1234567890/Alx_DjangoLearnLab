# 🛠️ CRUD Operations in Django Shell

This document includes the commands and expected output for performing Create, Retrieve, Update, and Delete operations on a `Book` model in the Django shell.

---

## 📘 Create a Book Instance

```python
>>> from bookshelf.models import Book

>>> book = Book.objects.create(
...     title="1984",
...     author="George Orwell",
...     publication_year=1949
... )

>>> print(book)
# Output: 1984 by George Orwell (1949)
```

---

## 🔍 Retrieve Book Instance

```python
>>> from bookshelf.models import Book

>>> book = Book.objects.get(title="1984")

>>> print(book.title)
# Output: 1984

>>> print(book.author)
# Output: George Orwell

>>> print(book.publication_year)
# Output: 1949
```

---

## ✏️ Update Book Title

```python
>>> book = Book.objects.get(title="1984")

>>> book.title = "Nineteen Eighty-Four"

>>> book.save()

>>> print(book.title)
# Output: Nineteen Eighty-Four
```

---

## 🗑️ Delete Book Instance and Confirm

```python
>>> book = Book.objects.get(title="Nineteen Eighty-Four")

>>> book.delete()
# Output: (1, {'bookshelf.Book': 1})

>>> Book.objects.all()
# Output: <QuerySet []>
```
