from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .decorators import *
from .utils import * 
from django.template.loader import get_template, render_to_string
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
import os
from passporteye import read_mrz
import pytesseract
# Create your views here.



@admin_only
def index(request):
    return render(request,"index.html")


def dashboard(request):
    return render(request,"index.html")


@unauthenticated_user
def loginPage(request):
    if request.user.is_authenticated:
            return redirect('dashboard')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,'Kullanıcı Adı veya Şifre yanlış')
        return render(request,"login.html")

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                
                messages.success(request,'Kayıt Başarılı')
                return redirect('login')
    context = {'form':form}
    return render(request,'register.html',context)


def logoutUser(request):
    logout(request)
    return redirect('dashboard')




def ensitumudur(request):
    return render(request,'ensitumudur.html')

def anabilim(request):
    return render(request,'anabilim.html')

def ensitu(request):
    return render(request,'ensitu.html')

def danisman(request):
    status = "Process"
    petition = ForeignStudentApplicationForm.object.filter(status=status)

    if request.method == "POST":
        id = ForeignStudentApplicationForm.object.filter(status=status).values('id')

        i = 0
        id_list = []
        for i in range(len(petition)):
            petition_id = str(id[i])
            petition_id = petition_id.replace("{'id': ","")
            petition_id = petition_id.replace("}","")
            id_list.append(petition_id)
        
        for i in range(len(id_list)):
            control = passport_control_api(id_list[i])
            if control == "Pasaport kriterlere uygun değil":
                status = "Mistaken"
                ForeignStudentApplicationForm.object.filter(id=id_list[i]).update(status=status)
                print(control,id_list[i])

        
    

    return render(request,'danisman.html',{'categoryies':petition})

def ogrenci(request):
    
    return render(request,'ogrenci.html')

def petitionShow(request,id):
    petition = ForeignStudentApplicationForm.object.get(id=id)

    status = "Ensitu"

    context = {'petition':petition}
    
    if request.method == 'POST':
        ForeignStudentApplicationForm.object.filter(id=id).update(status=status)
        return redirect('danisman')

    return render(request,'petition_show.html',context)

def mistakenPetition(request):
    status = "Mistaken"
    petition = ForeignStudentApplicationForm.object.filter(status=status)
    print("sadasd",petition)

    context = {'petition':petition}

    return render(request,'mistaken.html',context)


@login_required(login_url='login')
def mistakenStudentPetition(request):
    status = "Mistaken"
    id = request.user.student
    petition = ForeignStudentApplicationForm.object.filter(user=id,status=status)
    print("sadasd",id)

    context = {'petition':petition}

    return render(request,'mistaken.html',context)






@login_required(login_url='login')
def petition(request):
    ogrenci = request.user.student

    phd_status = "PhD"
    phd = Department.object.filter(institutes=phd_status)

    graduate_status = "Graduate"
    graduate = Department.object.filter(institutes=graduate_status)

    print(phd)


    if request.method == 'POST' :
        name = request.POST["name"]
        surname = request.POST["surname"]
        phonenumber = request.POST["phonenumber"]
        email = request.POST["email"]
        department = request.POST["department"]
        passport = request.FILES["passport"]
        graduation_document = request.FILES["graduation_document"]
        transcript = request.FILES["transcript"]
        language_document = request.FILES["language_document"]
        description = request.POST["description"]

        document = ForeignStudentApplicationForm.object.create(
            user=ogrenci,
            name=name,
            surname=surname,  
            phonenumber=phonenumber,
            email=email,
            department=department,
            passport=passport,
            graduation_document=graduation_document,
            transcript=transcript,
            language_document=language_document,
            description=description,
        )
        document.save()
        print(passport)
        return redirect('ogrenci')
    
    context = {'phd':phd,'graduate':graduate}
    
    return render(request,'asd.html',context)

def control(request,id):

    passport_control_api(id)
        
    return render(request,'anabilim.html')

