# Generated by Django 4.2.4 on 2023-08-14 00:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("collection", "0015_alter_book_publication_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="books",
            field=models.ManyToManyField(to="collection.book"),
        ),
    ]
