from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Petition



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class FileForm(forms.ModelForm):
    class Meta:
        model = Petition
        fields = "__all__"
        exclude = ['user']
