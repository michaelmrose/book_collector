from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Book
from .models import Author

bookList = [
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "published": "1965",
        "isbn": "0441013597",
    },
    {
        "title": "Starfish",
        "author": "Peter Watts",
        "published": "1999",
        "isbn": "0812575857",
    },
    {
        "title": "The Gone World",
        "author": "Tom Sweterlitsch",
        "published": "2018",
        "isbn": "0399167501",
    },
]


# Create your views here.
def home(request):
    return render(request, "home.html")


def books_index(request):
    return render(request, "books/index.html", {"books": Book.objects.all()})


def about(request):
    return render(request, "about.html")


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "books/detail.html", {"book": book})


class AuthorList(ListView):
    model = Author
    fields = "__all__"


class AuthorDetails(DetailView):
    model = Author


class AuthorCreate(CreateView):
    model = Author
    fields = ["name"]
    success_url = "/authors/"


class AuthorDelete(DeleteView):
    model = Author
    success_url = "/authors/"


class AuthorUpdate(UpdateView):
    model = Author
    fields = ["name"]
    success_url = "/authors/"
