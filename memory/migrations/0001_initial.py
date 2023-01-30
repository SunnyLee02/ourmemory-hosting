# Generated by Django 4.1.5 on 2023-01-19 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Memory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("placeName", models.TextField(default="")),
                ("placeRoad", models.TextField(default="")),
                ("placeAddress", models.TextField(default="")),
                ("placeX", models.TextField(default="")),
                ("placeY", models.TextField(default="")),
                ("feedDate", models.TextField(default="")),
                ("description", models.TextField(default="")),
                (
                    "image",
                    models.ImageField(default="media/default_image.jpeg", upload_to=""),
                ),
            ],
        ),
    ]
