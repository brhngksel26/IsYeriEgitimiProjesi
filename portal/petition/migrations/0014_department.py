# Generated by Django 3.0.8 on 2020-10-27 14:10

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0013_foreignstudentapplicationform_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('institutes', models.CharField(choices=[('Graduate', 'Yüksek Lisans'), ('PhD', 'Doktara')], max_length=100)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
