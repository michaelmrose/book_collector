from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.admin.widgets import AdminDateWidget
from django.urls import reverse_lazy

from .models import Book
from .models import Author


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

    # we are passsing next in the book form
    def get_success_url(self):
        # Redirect back to the previous page or default to the home page
        return self.request.GET.get("next", reverse_lazy("author_index"))


class AuthorDelete(DeleteView):
    model = Author
    success_url = "/authors/"


class AuthorUpdate(UpdateView):
    model = Author
    fields = ["name"]
    success_url = "/authors/"


class BookCreate(CreateView):
    model = Book
    fields = [
        "title",
        "description",
        "publicationDate",
        "isbn",
        "authors",
    ]
    success_url = "/books/"

    # thanks stackoverflow https://stackoverflow.com/questions/21405895/datepickerwidget-in-createview
    def get_form(self, form_class=None):
        form = super(BookCreate, self).get_form(form_class)
        form.fields["publicationDate"].widget = AdminDateWidget(attrs={"type": "date"})
        return form

    # I really want the book form to save and restore its data so that a partially filled out form can be retained
    # after a new author is added but can't get this feature working yet.


class BookDelete(DeleteView):
    model = Book
    success_url = "/books/"


class BookUpdate(UpdateView):
    model = Book
    fields = ["title", "description", "authors", "publicationDate", "isbn"]
    success_url = "/books/"
