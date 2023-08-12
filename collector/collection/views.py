from django.shortcuts import render, redirect
from .models import Book

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
