# Generated by Django 4.1.7 on 2023-05-04 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Machine",
            fields=[
                (
                    "id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("nom", models.CharField(max_length=200)),
            ],
        ),
    ]