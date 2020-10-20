from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=30,null=True)
    email=models.EmailField(null=True)
    phone=models.CharField(max_length=30,null=True)

    object = models.Manager()


    def __str__(self):
        return self.student_name


class Petition(models.Model):
    CATEGORY = (
        ('Ensitu','Ensitu'),
        ('Department','Department'),
        ('EnsituDirector','EnsituDirector'),
        ('Advisor','Advisor'),
    )
    user = models.ForeignKey(Student, null=True, blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,blank=True)
    petition = models.FileField()
    category = models.CharField(max_length=100,null=True,choices=CATEGORY)
    finished = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now ,blank=True )

    object = models.Manager()


    def __str__(self):
        return self.title

class ForeignStudentApplicationForm(models.Model):
    STATUS = (
        ('Process','İşlem Sırasında'),
        ('Ensitu','Ensitu İncelemesinde'),
        ('Department','Departman İncelemesinde'),
        ('EnsituDirector','Ensitu Direktörünün İncelemesinde'),
        ('Advisor','Danışman İncelemesinde'),
    )
    user = models.ForeignKey(Student, null=True, blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    surname = models.CharField(max_length=75)
    phonenumber = models.CharField(max_length=35)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    passport = models.FileField()
    graduation_document = models.FileField()
    language_document = models.FileField()
    transcript = models.FileField()
    description = models.TextField(max_length=1000,blank=True)
    status = models.CharField(max_length=100,null=True,choices=STATUS, default=STATUS[0][0])

    object = models.Manager()


    def __str__(self):
        return self.email