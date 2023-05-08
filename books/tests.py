from django.test import TestCase
from django.urls import reverse

from .models import Book


class BooksTestCase(TestCase):
    """
    Test
    """
    def test_no_books(self):
        response = self.client.get(reverse("books:list"))

        self.assertContains(response, "No books found.")

    def test_books_list(self):
        Book.objects.create(title="Book1", description="Description1", isbn="111111") # noqa
        Book.objects.create(title="Book2", description="Description2", isbn="222222") # noqa
        Book.objects.create(title="Book3", description="Description3", isbn="333333") # noqa

        response = self.client.get(reverse("books:list"))

        books = Book.objects.all()
        for book in books:
            self.assertContains(response, book.title)

    def test_detail_page(self):
        book = Book.objects.create(title="Book1", description="Description1", isbn="111111") # noqa

        response = self.client.get(reverse("book:deatail", kwargs={"id": book.id})) # noqa

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)
