from django.shortcuts import render, get_object_or_404
from . import models


def book_all(request):
    books = models.Book.objects.all()
    return render(request, "book_list.html", {"books": books})


def book_detail(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, "book_detail.html", {"book": book})

def book_author(request, full_name):
    author = get_object_or_404(models.Author, id=full_name)
    return render(request, "author.html", {"author": author})
