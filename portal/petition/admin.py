from django.contrib import admin
from .models import Petition,Student,ForeignStudentApplicationForm,Department

# Register your models here.

admin.site.register(Petition)
admin.site.register(Student)
admin.site.register(ForeignStudentApplicationForm)
admin.site.register(Department)