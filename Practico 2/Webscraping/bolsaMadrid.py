#Importamos la Librerias
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pandas as pd
from matplotlib import pyplot
import matplotlib

#Enlace de la Bolsa Madrid
url="https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000"
path='Practico 2/Webscraping/csv/bolsaMadrid.csv'

#Haremos el request a esa ruta
#Procesamos el HTML mediante BeautifulSoap
req = requests.get(url).text
soup = BeautifulSoup(req, "lxml")

# Obtenemos la tabla por un ID específico
table = soup.find("table", {"id":"ctl00_Contenido_tblAcciones"})

name=""
price=""
numRow=0

for row in table.find_all("tr"):
  numCell=0
  for cell in row.find_all("td"):
    if numCell == 0:
      name=cell.text
      print("Accion:", name)
    if numCell == 1:
      price=cell.text
      print("Ultimo:", price,'\n')
    numCell+=1
  numRow+=1
  #Creamos el CSV
  with open(path, 'a',  newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, price, datetime.now()])
  csv_file.close()


df = pd.read_csv(path)
#Creamos las columnas para el DataFrame
columnsName = ["Accion", "Precio", "Fecha"]
df.columns = columnsName

#Eliminamos Datos NaN
df = df.dropna()

#Convertimos en Precio es float
df['Precio'] = df['Precio'].apply(lambda x: x.replace(',','.'))
df['Precio'] = df['Precio'].astype(float)

#Calculamos Maximo y minimo
print("Mayor ganancia:", df['Precio'].max(), "\nMayor pérdida:", df['Precio'].min())

#Ordenamos la columna Precio
df=df.sort_values("Precio")
df.to_csv(path, index=False)
df


