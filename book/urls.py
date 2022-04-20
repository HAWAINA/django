from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name="hello"),
    path('books/', views.book_all, name="book_All"),
    path("books/<int:id>/", views.book_detail, name="book_detail"),
]
