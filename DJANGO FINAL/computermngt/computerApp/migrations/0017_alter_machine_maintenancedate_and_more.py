# Generated by Django 4.2 on 2023-06-02 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0016_alter_machine_maintenancedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 2, 17, 25, 13, 83818)),
        ),
        migrations.AlterField(
            model_name='machine',
            name='type_materiel',
            field=models.CharField(choices=[('PC', 'PC'), ('Mac', 'MAc'), ('Serveur', 'Serveur'), ('Switch', 'Switch'), ('Routeur', 'Routeur')], default='PC', max_length=32),
        ),
    ]
