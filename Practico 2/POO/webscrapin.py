import pandas as pd
import numpy as np

class webscraping:
    def __init__(self, url, table):
        self.url = url
        self.path = 'DatosWebscraping.csv'
        self.table_id = table
        self.df = pd.read_html(url, attrs=self.table_id, thousands='.', decimal=',')[0]

    def toCSV(self):
      '''Exporta datos en formato CSV.'''
      return self.df.to_csv(self.path)

    def toDF(self):
      '''Exporta datos en formato DataFrame'''
      return self.df

    def maximos(self, columna, cantidad):
      '''Devuelve la cantidad de maximos indicado del DataFrame indicando la columna'''
      resultado = self.df.sort_values(columna, ascending=False)
      return resultado.head(cantidad)

    def minimos(self, columna, cantidad):
      '''Devuelve la cantidad de minimos indicado del DataFrame indicando la columna'''
      resultado = self.df.sort_values(columna)
      return resultado.head(cantidad)