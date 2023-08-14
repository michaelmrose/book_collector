from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("books/", views.books_index, name="index"),
    path("books/<int:book_id>/", views.book_detail, name="detail"),
    path("books/create/", views.BookCreate.as_view(), name="book_create"),
    path("books/<int:pk>/delete/", views.BookDelete.as_view(), name="book_delete"),
    path("books/<int:pk>/update/", views.BookUpdate.as_view(), name="book_update"),
    # authors
    path("authors/", views.AuthorList.as_view(), name="author_index"),
    path("authors/<int:pk>/", views.AuthorDetails.as_view(), name="author_detail"),
    path("authors/create/", views.AuthorCreate.as_view(), name="author_create"),
    path(
        "authors/<int:pk>/delete/", views.AuthorDelete.as_view(), name="author_delete"
    ),
    path(
        "authors/<int:pk>/update/", views.AuthorUpdate.as_view(), name="authors_update"
    ),
    # series
    path("series/", views.SeriesList.as_view(), name="series_index"),
    path("series/<int:pk>/", views.SeriesDetails.as_view(), name="series_detail"),
    path("series/create/", views.SeriesCreate.as_view(), name="series_create"),
    path("series/<int:pk>/delete/", views.SeriesDelete.as_view(), name="series_delete"),
    path("series/<int:pk>/update/", views.SeriesUpdate.as_view(), name="series_update"),
    # tags
    path("tags/", views.TagList.as_view(), name="tags_index"),
    path("tags/<int:pk>/", views.TagDetails.as_view(), name="tag_detail"),
    path("tags/create/", views.TagCreate.as_view(), name="tag_create"),
    path("tags/<int:pk>/delete/", views.TagDelete.as_view(), name="tag_delete"),
    path("tags/<int:pk>/update/", views.TagUpdate.as_view(), name="tag_update"),
]
