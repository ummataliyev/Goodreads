from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from books.models import Book
from books.models import BookReview
from users.models import CustomUser


class BookReviewAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username="great",
            first_name="Djohn"
        )
        self.user.set_password("somepass")
        self.user.save()

    def test_book_review_detail(self):
        book = Book.objects.create(
            title="Book1",
            description="Description1",
            isbn="123121"
        )

        br = BookReview.objects.create(
            book=book,
            user=self.user,
            stars_given=5,
            comment="Fucking good;)"
        )
        response = self.client.get(reverse('api:review-detail', kwargs={'id': br.id})) # noqa

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], br.id)
        self.assertEqual(response.data['stars_given'], 5)
        self.assertEqual(response.data['comment'], "Fucking good;)")
