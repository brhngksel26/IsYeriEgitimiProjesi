from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import DownlandPDF,GetPDF,GeneratePdf
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('downland/', DownlandPDF.as_view(),name="downland"),
    path('get/', GetPDF.as_view(),name="get"),
    path('index/', views.index,name="index"),
    path('control/', views.test,name="test"),
    path('control', views.test,name="test"),
    path('', views.dashboard,name="dashboard"),
    path('login/',views.loginPage,name="login"),
    path('register/',views.registerPage,name="register"),
    path('upload/',views.uploadfile,name="upload"),
    path('ensitumudur/',views.ensitumudur,name="ensitumudur"),
    path('danisman/',views.danisman,name="danisman"),
    path('anabilim/',views.anabilim,name="anabilim"),
    path('ensitu/',views.ensitu,name="ensitu"),
    path('logout/',views.logoutUser,name="logout"),
    path('ogrenci/',views.ogrenci,name="ogrenci"),
    path('petitionshow/<id>',views.petitionShow,name="petitionShow"),
    path('petition/',views.petition,name="petition"),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)