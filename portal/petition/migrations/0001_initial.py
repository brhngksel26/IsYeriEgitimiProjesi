# Generated by Django 3.0.6 on 2020-10-12 07:17

import datetime
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('petition', models.FileField(upload_to='')),
                ('finished', models.BooleanField(default=False)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
