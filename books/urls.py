from django.urls import path

from books.views import AddReview
from books.views import BooksView
from books.views import BookDetailView

app_name = "books"
urlpatterns = [
    path("", BooksView.as_view(), name="list"),
    path("<int:id>/", BookDetailView.as_view(), name="detail"),
    path("<int:id>/reivews/", AddReview.as_view(), name="reviews")
]
