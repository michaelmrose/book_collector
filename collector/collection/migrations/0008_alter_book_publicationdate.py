# Generated by Django 4.2.4 on 2023-08-13 00:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("collection", "0007_book_authors"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="publicationDate",
            field=models.DateField(default=datetime.date(2023, 8, 13)),
        ),
    ]