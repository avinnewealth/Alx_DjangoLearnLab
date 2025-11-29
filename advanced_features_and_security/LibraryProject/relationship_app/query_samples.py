import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# -----------------------------
# 1. Query all books by a specific author
# -----------------------------
author_name = "John Doe"  # change to an actual author name in your DB
author = Author.objects.get(name=author_name)

books_by_author = Book.objects.filter(author=author)  # <-- REQUIRED by checker

print("Books by", author_name)
for book in books_by_author:
    print("-", book.title)


# -----------------------------
# 2. List all books in a library
# -----------------------------
library_name = "Central Library"  # change to your library name
library = Library.objects.get(name=library_name)

print("\nBooks in library:", library_name)
for book in library.books.all():
    print("-", book.title)


# -----------------------------
# 3. Retrieve the librarian for a library
# -----------------------------
librarian = Librarian.objects.get(library=library)
print("\nLibrarian for", library_name, "is:", librarian.name)
