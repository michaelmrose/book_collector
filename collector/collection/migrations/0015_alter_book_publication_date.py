# Generated by Django 4.2.4 on 2023-08-14 00:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("collection", "0014_alter_author_bio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="publication_date",
            field=models.DateField(default=datetime.date(2023, 8, 14)),
        ),
    ]