# Generated by Django 3.0.6 on 2020-10-21 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0012_auto_20201020_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreignstudentapplicationform',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
