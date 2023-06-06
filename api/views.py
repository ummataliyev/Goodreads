from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from books.models import BookReview
from api.serializers import BookReviewSerializer


class BookReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewSerializer
    queryset = BookReview.objects.all().order_by('-created_at')
    lookup_field = 'id'


# GENERIC from of View

# class BookReviewDetailApiView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = BookReviewSerializer
#     queryset = BookReview.objects.all()
#     lookup_field = 'id'


# class BookListAPIView(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = BookReviewSerializer
#     queryset = BookReview.objects.all().order_by('-created_at')


# Another form for BookReviewDetailApiView  using DRF

# class BookReviewDetailApiView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, id):
#         book_review = BookReview.objects.get(id=id)

#         serializer = BookReviewSerializer(book_review)

#         return Response(data=serializer.data)

#     def delete(self, request, id):
#         book_review = BookReview.objects.get(id=id)
#         book_review.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def put(self, request, id):
#         book_review = BookReview.objects.get(id=id)
#         serializer = BookReviewSerializer(instance=book_review, data=request.data) # noqa

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)

#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST) # noqa

#     def patch(self, request, id):
#         book_review = BookReview.objects.get(id=id)
#         serializer = BookReviewSerializer(
#             instance=book_review,
#             data=request.data,
#             partial=True
#         )

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)

#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST) # noqa


# class BookListAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     book_reviews = BookReview.objects.all().order_by('-created_at')

    #     paginator = PageNumberPagination()
    #     page_obj = paginator.paginate_queryset(book_reviews, request)
    #     serializer = BookReviewSerializer(page_obj, many=True)

    #     return paginator.get_paginated_response(serializer.data)

    # def post(self, request):
    #     serializer = BookReviewSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_201_CREATED) # noqa

    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST) # noqa

# Handmade Veiw

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
