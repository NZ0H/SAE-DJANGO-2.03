# Generated by Django 4.2 on 2023-05-11 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0009_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 5, 11, 7, 23, 49, 454362)),
        ),
    ]
