#Importar las librerias necesarias para hacer WebScripting
import pandas as pd
import requests
from bs4 import BeautifulSoup

#Obtener la URL de la pagina y su respuesta

url = "https://receptor.com.mx/2022/09/07/estadisticas-liga-mayor-onefa-2022"
r = requests.get(url)

#Crear una sopa con BeautifulSoap para encontrar los elementos que queremos

soup = BeautifulSoup(r.content,'html.parser')
columns = soup.find('table', attrs={"data-id":"168"}).find('thead').find('tr').find_all('th')
columns[0].get_text()

#Vamos a recorrer cada th para obtener el nombre de las columnas 

name_columns = []
for column in columns:
    name_columns.append(column.get_text())

#Obtener el valor de cada fila
rows = soup.find('table', attrs={"data-id":"168"}).find('tbody').find_all('tr')

equipos = []
juegos_jugados = []
puntos = []
ppj = []
yds_totales = []
yds_tot_partido = []
yds_pase = []
yds_pase_partido = []
yds_tierra = []
yds_tierra_partido = []
primeroy10 = []
primeroy10_pase = []
primeroy10_tierra = []
primeroy10_castigo = []
int_lanzadas = []
fumbles_perdidos = []
turnovers_totales = []
for row in rows:
    equipos.append(row.find_all('td')[0].get_text())
    juegos_jugados.append(row.find_all('td')[1].get_text())
    puntos.append(row.find_all('td')[2].get_text())
    ppj.append(row.find_all('td')[3].get_text())
    yds_totales.append(row.find_all('td')[4].get_text())
    yds_tot_partido.append(row.find_all('td')[5].get_text())
    yds_pase.append(row.find_all('td')[6].get_text())
    yds_pase_partido.append(row.find_all('td')[7].get_text())
    yds_tierra.append(row.find_all('td')[8].get_text())
    yds_tierra_partido.append(row.find_all('td')[9].get_text())
    primeroy10.append(row.find_all('td')[10].get_text())
    primeroy10_pase.append(row.find_all('td')[11].get_text())
    primeroy10_tierra.append(row.find_all('td')[12].get_text())
    primeroy10_castigo.append(row.find_all('td')[13].get_text())
    int_lanzadas.append(row.find_all('td')[14].get_text())
    fumbles_perdidos.append(row.find_all('td')[15].get_text())
    turnovers_totales.append(row.find_all('td')[16].get_text())

#Crear el Data Frame

data = pd.DataFrame({"Equipos":equipos,
                     "JJ":juegos_jugados,
                     "Puntos":puntos,
                     "PPJ":ppj,
                     "Yds_totales":yds_totales,
                     "Yds_tot/partido":yds_tot_partido,
                     "Yds_pase":yds_pase,
                     "Yds_pase/partido":yds_pase_partido,
                     "Yds_Tierra":yds_tierra,
                     "Yds_tierra/partido":yds_tierra_partido,
                     "1y10s":primeroy10,
                     "1y10s_pase":primeroy10_pase,
                     "1Y10s_Tierra":primeroy10_tierra,
                     "1y10s_castigo":primeroy10_castigo,
                     "Int_lanzadas": int_lanzadas,
                     "Fumbles_Perdidos":fumbles_perdidos,
                     "Turnovers_Totales":turnovers_totales,
                    })

#Crear el archivo CSV
data.to_csv('ONEFAOFENSIVA_22-10-31')


