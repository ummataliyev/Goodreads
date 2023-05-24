from django.urls import path

from books.views import AddReview
from books.views import BooksView
from books.views import BookDetailView
from books.views import EditReviewView
from books.views import DeleteReviewView
from books.views import ConfirmDeleteReviewView

app_name = "books"

urlpatterns = [
    path("", BooksView.as_view(), name="list"),
    path("<int:id>/", BookDetailView.as_view(), name="detail"),
    path("<int:id>/reivews/", AddReview.as_view(), name="reviews"),
    path("<int:book_id>/reviews/<int:review_id>/edit/", EditReviewView.as_view(), name="edit-review"), # noqa
    path("<int:book_id>/reviews/<int:review_id>/delete/confirm/", ConfirmDeleteReviewView.as_view(), name="confirm-delete-review"), # noqa
    path("<int:book_id>/reviews/<int:review_id>/delete/", DeleteReviewView.as_view(), name="delete-review"), # noqa
]
