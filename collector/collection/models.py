from django.db import models
from django.db.models import Q
from django.core.validators import RegexValidator
from datetime import date

# Create your models here.

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
        books = models.ManyToManyField(Book)

class Book(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=100)
    isbn = models.CharField(
        max_length=10,
        validators=[RegexValidator("\d{10}", message="ISBN are 10 numeric characters")],
    )
    authors = models.ManyToManyField(Author)
    publicationDate = models.DateField(default=date.today())
    description = models.TextField(max_length=1000, default="")


