
---

# 📄 **delete.md**

```md
# DELETE Operation

## Command:
```python

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()

[]
# Book deleted successfully; no books remain.
