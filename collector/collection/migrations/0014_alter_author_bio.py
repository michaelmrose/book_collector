# Generated by Django 4.2.4 on 2023-08-13 21:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("collection", "0013_book_number_in_series_book_series"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="bio",
            field=models.TextField(default="", max_length=1000),
        ),
    ]
