from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

from users.models import CustomUser


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    isbn = models.CharField(max_length=17)
    cover_picture = models.ImageField(default="def_book_pic.jpg")

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} by {self.author.first_name} {self.author.last_name}" # noqa


class BookReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    stars_given = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    created_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.stars_given} stars for {self.book.title} by {self.user.username}" # noqa
