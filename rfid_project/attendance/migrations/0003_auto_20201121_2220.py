# Generated by Django 3.1.2 on 2020-11-21 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20200504_1638'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Client',
        ),
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 11, 21, 22, 20, 43, 281650)),
        ),
        migrations.AlterField(
            model_name='log',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2020, 11, 21, 22, 20, 43, 281650)),
        ),
    ]