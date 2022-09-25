# Generated by Django 4.1.1 on 2022-09-25 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("create_date", models.DateTimeField(auto_now=True)),
                ("author", models.CharField(max_length=100)),
            ],
        ),
    ]
