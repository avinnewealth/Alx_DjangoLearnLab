
---

# 📄 **delete.md**

```md
# DELETE Operation

## Command:
```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()

[]
# Book deleted successfully; no books remain.
