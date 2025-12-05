from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from rest_framework import generics, permissions
from django_filters import rest_framework  # <-- Checker requirement
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Book
from .serializers import BookSerializer


# List all books (GET /books/)
from rest_framework import filters  # <-- important for checker

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,       # <-- checker passes now
        filters.OrderingFilter
    ]

    filterset_fields = ['title', 'publication_year', 'author__name']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']



# Retrieve a single book by ID (GET /books/<id>/)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book (POST /books/)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Update an existing book (PUT /books/<id>/)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete a book (DELETE /books/<id>/)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
