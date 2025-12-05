from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user for authenticated tests
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create sample books
        self.book1 = Book.objects.create(title="Alpha", publication_year=2001)
        self.book2 = Book.objects.create(title="Beta", publication_year=1999)

        self.client = APIClient()

        # URLs
        self.list_url = reverse("book-list")
        self.create_url = reverse("book-create")
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book1.id})
        self.update_url = reverse("book-update", kwargs={"pk": self.book1.id})
        self.delete_url = reverse("book-delete", kwargs={"pk": self.book1.id})

    # -------------------------------
    # Test LIST endpoint
    # -------------------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # -------------------------------
    # Test DETAIL endpoint
    # -------------------------------
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # -------------------------------
    # Test CREATE (requires auth)
    # -------------------------------
    def test_create_book_unauthenticated(self):
        response = self.client.post(self.create_url, {"title": "New Book", "publication_year": 2024})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")

        response = self.client.post(self.create_url, {"title": "New Book", "publication_year": 2024})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # -------------------------------
    # Test UPDATE (requires auth)
    # -------------------------------
    def test_update_book_unauthenticated(self):
        response = self.client.put(self.update_url, {"title": "Updated Title", "publication_year": 2005})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="password123")

        response = self.client.put(self.update_url, {"title": "Updated", "publication_year": 2002})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_book = Book.objects.get(id=self.book1.id)
        self.assertEqual(updated_book.title, "Updated")

    # -------------------------------
    # Test DELETE (requires auth)
    # -------------------------------
    def test_delete_book_unauthenticated(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="password123")

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # -------------------------------
    # Filtering Tests
    # -------------------------------
    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url + "?title=Alpha")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Alpha")

    def test_filter_books_by_publication_year(self):
        response = self.client.get(self.list_url + "?publication_year=1999")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["publication_year"], 1999)

    # -------------------------------
    # Search Tests
    # -------------------------------
    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Alpha")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Alpha")

    # -------------------------------
    # Ordering Tests
    # -------------------------------
    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url + "?ordering=publication_year")
        self.assertEqual(response.data[0]["publication_year"], 1999)

    def test_order_books_descending(self):
        response = self.client.get(self.list_url + "?ordering=-publication_year")
        self.assertEqual(response.data[0]["publication_year"], 2001)
