from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.admin.widgets import AdminDateWidget
from django.urls import reverse_lazy

from .models import Book
from .models import Author
from .models import Series
from .models import Tag


# Create your views here.
def home(request):
    return render(request, "home.html")


def books_index(request):
    return render(request, "books/index.html", {"books": Book.objects.all()})


def about(request):
    return render(request, "about.html")


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    all_tags = set(Tag.objects.all())
    available_tags = list(all_tags.difference(book.tags.all()))
    return render(
        request,
        "books/detail.html",
        {"book": book, "available_tags": available_tags},
    )


class AuthorList(ListView):
    model = Author
    fields = "__all__"


class AuthorDetails(DetailView):
    model = Author


class AuthorCreate(CreateView):
    model = Author
    fields = ["name", "bio", "primary_genre"]

    # we are passsing next in the book form
    def get_success_url(self):
        # Redirect back to the previous page or default to the home page
        return self.request.GET.get("next", reverse_lazy("author_index"))


class AuthorDelete(DeleteView):
    model = Author
    success_url = "/authors/"


class AuthorUpdate(UpdateView):
    model = Author
    fields = ["name", "bio", "primary_genre"]
    success_url = "/authors/"


class BookCreate(CreateView):
    model = Book
    fields = [
        "title",
        "series",
        "number_in_series",
        "description",
        "publication_date",
        "isbn",
        "authors",
        "tags",
    ]
    success_url = "/books/"

    # thanks stackoverflow https://stackoverflow.com/questions/21405895/datepickerwidget-in-createview
    def get_form(self, form_class=None):
        form = super(BookCreate, self).get_form(form_class)
        form.fields["publication_date"].widget = AdminDateWidget(attrs={"type": "date"})
        return form

    # I really want the book form to save and restore its data so that a partially filled out form can be retained
    # after a new author is added but can't get this feature working yet.


class BookDelete(DeleteView):
    model = Book
    success_url = "/books/"


class BookUpdate(UpdateView):
    model = Book
    fields = [
        "title",
        "series",
        "number_in_series",
        "description",
        "publication_date",
        "isbn",
        "authors",
        "tags",
    ]
    success_url = "/books/"

    def get_form(self, form_class=None):
        form = super(BookUpdate, self).get_form(form_class)
        form.fields["publication_date"].widget = AdminDateWidget(attrs={"type": "date"})
        return form


# series


class SeriesList(ListView):
    model = Series
    fields = "__all__"


class SeriesDetails(DetailView):
    model = Series


class SeriesCreate(CreateView):
    model = Series
    fields = "__all__"

    # we are passsing next in the book form
    def get_success_url(self):
        # Redirect back to the previous page or default to the home page
        return self.request.GET.get("next", reverse_lazy("series_index"))


class SeriesDelete(DeleteView):
    model = Series
    success_url = "/series/"


class SeriesUpdate(UpdateView):
    model = Series
    fields = "__all__"
    success_url = "/series/"


# tags


class TagList(ListView):
    model = Tag
    fields = "__all__"


class TagDetails(DetailView):
    model = Tag


class TagCreate(CreateView):
    model = Tag
    fields = "__all__"

    # we are passsing next in the book form
    def get_success_url(self):
        # Redirect back to the previous page or default to the home page
        return self.request.GET.get("next", reverse_lazy("tags_index"))


class TagDelete(DeleteView):
    model = Tag
    success_url = "/tags/"


class TagUpdate(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = "/tags/"


def associate_tag(request, book_id, tag_id):
    Book.objects.get(id=book_id).tags.add(tag_id)
    return redirect("detail", book_id=book_id)


def disassociate_tag(request, book_id, tag_id):
    Book.objects.get(id=book_id).tags.remove(tag_id)
    return redirect("detail", book_id=book_id)
