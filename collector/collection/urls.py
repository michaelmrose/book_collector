from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("books", views.books_index, name="index"),
    path("books/<int:book_id>/", views.book_detail, name="detail"),
    path("authors/", views.AuthorList.as_view(), name="author_index"),
    path("authors/<int:pk>/", views.AuthorDetails.as_view(), name="author_detail"),
    path("authors/create/", views.AuthorCreate.as_view(), name="author_create"),
    path(
        "authors/<int:pk>/delete/", views.AuthorDelete.as_view(), name="author_delete"
    ),
    path(
        "authors/<int:pk>/update/", views.AuthorUpdate.as_view(), name="authors_update"
    ),
]
