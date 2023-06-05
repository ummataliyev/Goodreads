from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from books.models import BookReview
from api.serializers import BookReviewSerializer


class BookReviewDetailApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        book_review = BookReview.objects.get(id=id)

        serializer = BookReviewSerializer(book_review)

        return Response(data=serializer.data)


class BookListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        book_reviews = BookReview.objects.all().order_by('-created_at')

        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(book_reviews, request)
        serializer = BookReviewSerializer(page_obj, many=True)

        return paginator.get_paginated_response(serializer.data)


# Another for BookReviewDetailApiView

# class BookReviewDetailApiView(View):
#     def get(self, request, id):
#         json_response = {}
#         try:
#             book_review = BookReview.objects.get(id=id)
#             json_response["id"] = book_review.id
#             json_response["comment"] = book_review.comment
#             json_response["stars_given"] = book_review.stars_given

#             json_response["book"] = {
#                 "id": book_review.book.id,
#                 "title": book_review.book.title,
#                 "description": book_review.book.description,
#                 "isbn": book_review.book.isbn
#             }

#             json_response["user"] = {
#                 "id": book_review.user.id,
#                 "first_name": book_review.user.first_name,
#                 "last_name": book_review.user.last_name,
#                 "username": book_review.user.username,

#             }

#         except BookReview.DoesNotExist as error:
#             logger.error(f"error was occured: {error}")
#             json_response["error"] = "Book does not exist("

#         return JsonResponse(json_response)
