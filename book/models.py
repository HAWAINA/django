from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='')
    author = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class BookFeedBack(models.Model):
    text = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    books = models.ForeignKey(Book,
                              on_delete=models.CASCADE,
                              related_name="Book_feed_back")

    def __str__(self):
        return self.books.title


class Author(models.Model):
    GENDER = (
        ("male", "MALE"),
        ("female", "FEMALE"),
    )
    name = models.TextField(max_length=80)
    date_birth = models.TextField()
    story = models.TextField()
    gender = models.CharField(max_length=20, choices=GENDER)
    author = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_author")

    def __str__(self):
        return self.book.author
