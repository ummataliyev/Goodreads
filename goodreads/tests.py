from django.test import TestCase
from django.urls import reverse

from books.models import Book
from books.models import BookReview
from users.models import CustomUser


class HomePageTestCase(TestCase):
    def test_paginated_list(self):
        book = Book.objects.create(
            title="Book1",
            description="Description1",
            isbn="777777"
            )
        user = CustomUser.objects.create(
            username="somebody",
            first_name="Somebody",
            last_name="Somebodiev",
            email="somebody@gamil.com"
        )
        user.set_password("somebody")
        user.save()
        review1 = BookReview.objects(book=book,user=user, stars_given=3, comment="Very good book") # noqa
        review2 = BookReview.objects(book=book, user=user, stars_given=4, comment="Useful book") # noqa
        review3 = BookReview.objects(book=book, user=user, stars_given=5, comment="Fucking book") # noqa

        response = self.client.get(reverse("home_page") + "?page_size=2")

        self.assertContains(response, review3.comment)
        self.assertContains(response, review2.comment)
        self.assertContains(response, review1.comment)
