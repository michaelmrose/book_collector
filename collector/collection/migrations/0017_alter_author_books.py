# Generated by Django 4.2.4 on 2023-08-14 00:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("collection", "0016_alter_author_books"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="books",
            field=models.ManyToManyField(blank=True, null=True, to="collection.book"),
        ),
    ]
