# Generated by Django 4.1.1 on 2022-09-25 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(
                default=models.CharField(max_length=200), max_length=200
            ),
        ),
    ]
