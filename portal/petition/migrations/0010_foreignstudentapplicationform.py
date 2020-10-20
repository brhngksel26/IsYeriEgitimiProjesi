# Generated by Django 3.0.6 on 2020-10-20 18:50

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0009_petition_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeignStudentApplicationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('surname', models.CharField(max_length=75)),
                ('phonenumber', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=100)),
                ('passport', models.FileField(upload_to='')),
                ('graduation_document', models.FileField(upload_to='')),
                ('language_document', models.FileField(upload_to='')),
                ('transcript', models.FileField(upload_to='')),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('status', models.CharField(choices=[('Process', 'İşlem Sırasında'), ('Ensitu', 'Ensitu İncelemesinde'), ('Department', 'Departman İncelemesinde'), ('EnsituDirector', 'Ensitu Direktörünün İncelemesinde'), ('Advisor', 'Danışman İncelemesinde')], default='Process', max_length=100, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='petition.Student')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]