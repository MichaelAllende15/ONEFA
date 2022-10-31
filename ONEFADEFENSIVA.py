#Importar librerias
import pandas as pd
import requests
from bs4 import BeautifulSoup

#Obtener respuesta de la pagina we consultada
url = "https://receptor.com.mx/2022/09/07/estadisticas-liga-mayor-onefa-2022"
r = requests.get(url)

#Crear una sopa con BeautifulSoup para encontrar los elementos
soup = BeautifulSoup(r.content,'html.parser')
columns = soup.find('table', attrs={"data-id":"169"}).find('thead').find('tr').find_all('th')

#Iterar por cada uno de los th para optener las columnas 
column_names = []
for column in columns:
    column_names.append(column.get_text())

# Obtener el valor de cada fila
rows = soup.find('table',attrs={"data-id":"169"}).find('tbody').find_all('tr')

equipo = []
jj = []
pts_perm = []
pppj = []
yds_tot = []
yds_tot_partido = []
yds_pase = []
yds_pase_partido = []
yds_tierra = []
yds_tierra_partido = []
primeroy10_perm = []

for row in rows:
    equipo.append(row.find_all('td')[0].get_text())
    jj.append(row.find_all('td')[1].get_text())
    pts_perm.append(row.find_all('td')[2].get_text())
    pppj.append(row.find_all('td')[3].get_text())
    yds_tot.append(row.find_all('td')[4].get_text())
    yds_tot_partido.append(row.find_all('td')[5].get_text())
    yds_pase.append(row.find_all('td')[6].get_text())
    yds_pase_partido.append(row.find_all('td')[7].get_text())
    yds_tierra.append(row.find_all('td')[8].get_text())
    yds_tierra_partido.append(row.find_all('td')[9].get_text())
    primeroy10_perm.append(row.find_all('td')[10].get_text())

# Crear el data frame

data = pd.DataFrame({"Equipos":equipo,
                    "JJ": jj,
                    "Pts Perm": pts_perm,
                    "PPPJ": pppj,
                    "Yds Tot": yds_tot,
                    "Yds tot/partido": yds_tot_partido,
                    "Yds Pase": yds_pase,
                    "Yds Pase/partido": yds_pase_partido,
                    "Yds Tierra": yds_tierra,
                    "Yds Tierr/partido": yds_tierra_partido,
                    "1Y10S Perm":primeroy10_perm
                    })

data.to_csv('ONEFADEFENSIVA_22-31-10')
