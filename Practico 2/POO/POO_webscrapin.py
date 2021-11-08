import pandas as pd
import numpy as np

class webscraping:
    def __init__(self, url, table):
        self.url = url
        self.path = 'DatosWebscraping.csv'
        self.table_id = table
        self.df = pd.read_html(url, attrs=self.table_id, thousands='.', decimal=',', flavor=None)[0]
        self.df = self.df.drop(['Efectivo (miles €)', 'Hora'], axis=1)
        columnsName = ["Accion", "Cierre", "Diferencia", "Maximo", "Minimo", "Volumen", "Fecha"]
        self.df.columns = columnsName

    def toCSV(self):
      '''Exporta datos en formato CSV.'''
      return self.df.to_csv(self.path)

    def toDF(self):
      '''Exporta datos en formato DataFrame'''
      return self.df

    def maximos(self, columna, cantidad):
      '''Devuelve la cantidad de maximos indicado del DataFrame indicando la columna'''
      resultado = self.df.sort_values(columna, ascending=False)
      resultado = resultado.head(cantidad).to_dict('records')
      resultado = list(map(lambda x: 'Ganancia maxima del día de {0}: {1}'.format(x['Accion'], x[columna]), resultado))
      return '\n'.join(resultado)

    def minimos(self, columna, cantidad):
      '''Devuelve la cantidad de minimos indicado del DataFrame indicando la columna'''
      resultado = self.df.sort_values(columna)
      resultado = resultado.head(cantidad).to_dict('records')
      resultado = list(map(lambda x: 'Mayor perdida del día de {0}: {1}'.format(x['Accion'], x[columna]), resultado))
      return '\n'.join(resultado)