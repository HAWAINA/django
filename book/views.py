from django.shortcuts import render
from django.http import HttpResponse
from . import models


def hello_world():
    return HttpResponse("<h2>Hello World</h2>")


def book_all(request):
    book = models.Book.objects.all()
    return render(request, "figma.html", {"book": book})
