# Generated by Django 4.2.4 on 2023-08-14 00:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("collection", "0017_alter_author_books"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="author",
            name="books",
        ),
    ]