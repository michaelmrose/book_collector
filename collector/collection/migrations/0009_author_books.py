# Generated by Django 4.2.4 on 2023-08-13 00:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("collection", "0008_alter_book_publicationdate"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="books",
            field=models.ManyToManyField(to="collection.book"),
        ),
    ]