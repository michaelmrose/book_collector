from django.shortcuts import render, redirect

bookList = [
    {"title": "Dune", "author": "Frank Herbert", "published": "1965"},
    {"title": "Starfish", "author": "Peter Watts", "published": "1999"},
    {"title": "The Gone World", "author": "Tom Sweterlitsch", "published": 2018},
]


# Create your views here.
def home(request):
    return render(request, "home.html")


def books_index(request):
    return render(request, "books/index.html", {"books": bookList})


def about(request):
    return render(request, "about.html")
