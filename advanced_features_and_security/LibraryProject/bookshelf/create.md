# CREATE Operation

## Command:
```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
<Book: 1984>
# A new Book instance is successfully created.
