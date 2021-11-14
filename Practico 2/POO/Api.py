import pandas as pd

class Api:

  def __init__(self, tickers):
      self._path = 'Practico 2/POO/csv/{0}.csv'
      self._tickers = list(tickers.split())
      self._df = pd.DataFrame()

  def _crearDF(self):
    pass

  def toCSV(self, name):
    '''Exporta datos en formato CSV.'''
    return self._df.to_csv(self._path.format(name))

  def toDF(self):
    '''Exporta datos en formato DataFrame'''
    return self._df

  def _toStr(self, records, params, columna):
    '''Convierte en string los datos enviados'''
    resultado = list(map(lambda x: 'Valores {2} del día - {0}: {1:.3f}'.format(x['Accion'], float(x[columna]), params), records))
    return '\n'.join(resultado)

  def maximos(self, columna, cantidad):
    '''Devuelve la cantidad de maximos indicado del DataFrame indicando la columna'''
    resultado = self._df.sort_values(columna, ascending=False).head(cantidad).to_dict('records')
    return self._toStr(resultado, self.maximos.__name__ , columna)

  def minimos(self, columna, cantidad):
    '''Devuelve la cantidad de minimos indicado del DataFrame indicando la columna'''
    resultado = self._df.sort_values(columna).head(cantidad).to_dict('records')
    return self._toStr(resultado, self.minimos.__name__, columna)