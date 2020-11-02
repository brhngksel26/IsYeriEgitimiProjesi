from bs4 import BeautifulSoup
import requests
import numpy as np

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
print(yuksek_lisans)
print("*********************************")
print(doktora)

