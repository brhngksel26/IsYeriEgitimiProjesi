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

# Create your views here.



class DownlandPDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('asd.html')
        context = {
            "Adı Soyadı" : "Burhan",
            "Doğum Tarihi" : "2020-10-09",
            "Cinsiyet" : "ERKEK",
            "E-Posta Adresi ": "email@info.com",
            "Telefon" : "5342433147",
            "Mezuniyet Durumu" : "Lise",
            "İngilizce Seviyeniz" : "İleri Seviye",
            "Çalışmak İstediğiniz Pozisyon" : "Bilgi İşlem",
            "Askerlik Durumu"	: "Muaf",
            "Ek Bilgi" : "asdasdasd",
        }
        html = template.render(context)
        pdf = render_to_pdf('asd.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "test_%s.pdf" %("12341231")
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse(html)


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': "11.03.1998", 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('asd.html', data)
        return HttpResponse(pdf, content_type='application/pdf')    

class GetPDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('asd.html')
        context={}
        html = template.render(context)
        pdf = render_to_pdf('control.html', context)
        if request.method == "POST":
            template = get_template('control.html')
            context = {"Adı Soyadı" : "Burhan",
            "Doğum Tarihi" : "2020-10-09",
            "Cinsiyet" : "ERKEK",
            "E-Posta Adresi ": "email@info.com",
            "Telefon" : "5342433147",
            "Mezuniyet Durumu" : "Lise",
            "İngilizce Seviyeniz" : "İleri Seviye",
            "Çalışmak İstediğiniz Pozisyon" : "Bilgi İşlem",
            "Askerlik Durumu"	: "Muaf",
            "Ek Bilgi" : "asdasdasd",}
            html = template.render(context)
            pdf = render_to_pdf('asd.html', context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "test_%s.pdf" %("12341231")
                content = "inline; filename='%s'" %(filename)
                download = request.GET.get("download")
                if download:
                    content = "attachment; filename='%s'" %(filename)
                response['Content-Disposition'] = content
                return response
            return HttpResponse(html)
        return HttpResponse(pdf, content_type='application/pdf')


def index(request):
    return render(request,"test.html")

def test(request):
    #return render(request,"control.html")
    context = {}
    name = request.POST.get('name', None)
    birthday = request.POST.get('birthday', None)
    gender = request.POST.get('gender', None)
    email = request.POST.get('email', None)
    phonenumber = request.POST.get('phonenumber', None)
    graduation = request.POST.get('graduation', None)
    language_level = request.POST.get('language_level', None)
    position = request.POST.get('position', None)
    military_status = request.POST.get('military_status', None)
    description = request.POST.get('description', None)
    context['name'] = name
    context['birthday'] = birthday
    context['gender'] = gender
    context['email'] = email
    context['phonenumber'] = phonenumber
    context['graduation'] = graduation
    context['language_level'] = language_level
    context['position'] = position
    context['military_status'] = military_status
    context['description'] = description
    return render(request,'control.html',context)




@admin_only
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
                return redirect('dashboard')
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
    return redirect('index')


@login_required(login_url='login')
#@allowed_users(allowed_roles=['ogrenci'])
def uploadfile(request):
    ogrenci = request.user.student

    print(ogrenci)
    #,instance=ogrenci
    form = FileForm()

    if request.method == 'POST' :
        title = request.POST["title"]
        description = request.POST["description"]
        petition = request.FILES["petition"]
        finished = request.POST["finished"]
        document = Petition.object.create(
            user=ogrenci,
            title=title,
            description=description,  
            petition=petition,
            finished=finished,
        )
        document.save()
        return HttpResponse("Dosya eklendi")
        """form = FileForm(request.POST, request.FILES,instance=request.user.student)
        if form.is_valid():
            form.save()"""

    context={'form':form}
    return render(request,'fileupload.html',context)

def ensitumudur(request):
    return render(request,'ensitumudur.html')

def anabilim(request):
    return render(request,'anabilim.html')

def ensitu(request):
    return render(request,'ensitu.html')

def danisman(request):
    category = 'Advisor'
    petition = Petition.object.filter(category=category)
    print(petition.data)
    return render(request,'danisman.html',{'categoryies':petition})

def ogrenci(request):
    return render(request,'ogrenci.html')

def petitionShow(request):
    return render(request,'petition_show.html')


def deneme(request):
    if request.method == 'POST':
        petition = request.FILES["petition"]
        cvName = [el['CV'] for el in petition]
        file = cvName[len(cvName)-1]
        handle_uploaded_file(file)
    return render(request,'deneme.html')

@login_required(login_url='login')
def petition(request):
    ogrenci = request.user.student

    print(ogrenci)
    #,instance=ogrenci

    if request.method == 'POST' :
        name = request.POST["name"]
        surname = request.POST["surname"]
        phonenumber = request.POST["phonenumber"]
        email = request.POST["email"]
        department = request.POST["department"]
        passport = request.FILES["passport"]
        graduation_document = request.POST["graduation_document"]
        transcript = request.POST["transcript"]
        language_document = request.POST["language_document"]
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
        return redirect('ogrenci')
    
    
    return render(request,'asd.html')
