#!pip3 install investpy
import investpy
import pandas as pd

#Obtener la tabla en tiempo real de la bolsa de españa
df = investpy.get_stock_historical_data(country='spain')
df.to_csv(path2='Practico 2/Webscraping/csv/investpySpain.csv')
print(df)