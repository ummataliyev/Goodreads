from django.urls import path

from api.views import BookListAPIView
from api.views import BookReviewDetailApiView

app_name = "api"

urlpatterns = [
    path('reviews/', BookListAPIView.as_view(), name="review-list"),
    path('reviews/<int:id>/', BookReviewDetailApiView.as_view(), name='review-detail') # noqa
]
