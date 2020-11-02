from __future__ import unicode_literals

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from passporteye import read_mrz

from .models import Department,ForeignStudentApplicationForm
import os
from django.conf import settings
from django.test.signals import setting_changed
from bs4 import BeautifulSoup
import requests
import numpy as np
from cv2 import cv2



def department():
    Department.object.all().delete()

    url = "http://fbe.firat.edu.tr/tr/node/185"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find("table")
    table_rows =  table.find_all("tr")
    row_list = []

    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        row_list.append(row)


    anabilim_temiz = row_list[2::]
    for i in range(len(anabilim_temiz)):
        for j in range(len(anabilim_temiz[i])):
            anabilim_temiz[i][j] = anabilim_temiz[i][j].strip().replace('\xa0',' ')

    doktora = []
    yuksek_lisans = []
    #doktora programı olanlar
    for i in range(len(anabilim_temiz)):
            yuksek_lisans.append(anabilim_temiz[i][1])
            if(anabilim_temiz[i][3] == "X"):

                doktora.append(anabilim_temiz[i][1])

    for i in range(len(yuksek_lisans)):
        institutes = "Graduate"
        department = Department.object.create(
            department=yuksek_lisans[i],
            institutes=institutes,  
        )
        department.save()

    for i in range(len(doktora)):
        institutes = "PhD"
        department = Department.object.create(
            department=doktora[i],
            institutes=institutes,  
        )
        department.save()
        

    
def  sharpen(filename):
    
    img1 = cv2.imread(filename,1)
    filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpen_img_1=cv2.filter2D(img1,-1,filter)

    return sharpen_img_1



def passport_control_api(id):
    test = ForeignStudentApplicationForm.object.get(id=id)
    
    mrz = read_mrz(test.passport.path)

    try:
        mrz_data = mrz.to_dict()
        result = "Pasaport kriterlere uygun"
        """print('Nationality :' + mrz_data['nationality'])
        print('Given Name :' + mrz_data['names'])
        print('Surname :' + mrz_data['surname'])
        print('Passport type :' + mrz_data['type'])
        print('Date of birth :' + mrz_data['date_of_birth'])
        print('ID Number :' + mrz_data['personal_number'])
        print('Gender :' + mrz_data['sex'])
        print('Expiration date :' + mrz_data['expiration_date'])"""
        return result
            
    except AttributeError:
        result = "Pasaport kriterlere uygun değil"

        return result





