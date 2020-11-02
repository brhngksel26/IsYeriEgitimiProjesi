from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index,name="index"),
    path('dashboard', views.dashboard,name="dashboard"),
    path('login/',views.loginPage,name="login"),
    path('register/',views.registerPage,name="register"),
    path('ensitumudur/',views.ensitumudur,name="ensitumudur"),
    path('danisman/',views.danisman,name="danisman"),
    path('anabilim/',views.anabilim,name="anabilim"),
    path('ensitu/',views.ensitu,name="ensitu"),
    path('logout/',views.logoutUser,name="logout"),
    path('ogrenci/',views.ogrenci,name="ogrenci"),
    path('petitionshow/<id>',views.petitionShow,name="petitionShow"),
    path('petition/',views.petition,name="petition"),
    path('deneme/<id>',views.control,name="deneme"),
    path('mistakenpetition/',views.mistakenPetition,name="mistakenPetition"),
    path('mistakenStudentpetition/',views.mistakenStudentPetition,name="mistakenStudentpetition"),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)