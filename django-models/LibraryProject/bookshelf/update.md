
---

# 📄 **update.md**

```md
# UPDATE Operation

## Command:
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book

<Book: Nineteen Eighty-Four>
# Title updated successfully.
