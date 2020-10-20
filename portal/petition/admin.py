from django.contrib import admin
from .models import Petition,Student,ForeignStudentApplicationForm

# Register your models here.

admin.site.register(Petition)
admin.site.register(Student)
admin.site.register(ForeignStudentApplicationForm)