from django.db import models
from django.db.models import Q
from django.core.validators import RegexValidator
from datetime import date

# Create your models here.

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(
        max_length=10,
        validators=[RegexValidator("\d{10}", message="ISBN are 10 numeric characters")],
    )
    # author
    publicationDate = models.DateField(default=date.today())
    # tags
