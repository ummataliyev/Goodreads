from django.views import View
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from books.models import Book


# CRUD
class BooksView(ListView):
    template_name = "books/list.html"
    queryset = Book.objects.all()
    context_object_name = "books"

# class BooksView(View):
#     def get(self, request):
#         books = Book.objects.all()

#         return render(request, "books/list.html", {"books": books})


class BookDetailView(DetailView):
    template_name = "books/detail.html"
    pk_url_kwarg = "id"
    model = Book


# class BookDetailView(View):
#     def get(self, request, id):
#         book = Book.objects.get(id=id)

#         return render(request, "books/detail.html", {"book": book})
