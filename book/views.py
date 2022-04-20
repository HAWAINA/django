from django.shortcuts import render, get_object_or_404
from . import models


def book_all(request):
    book = models.Book.objects.all()
    return render(request, "figma.html", {"book": book})


def book_detail(request, id):
    book = get_object_or_404(models.Book, id=id)
    return render(request, "book_detail.html", {"book": book})
