
---

# 📄 **retrieve.md**

```md
# RETRIEVE Operation

## Command:
```python
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year

('1984', 'George Orwell', 1949)
# Successfully retrieved the created book.
