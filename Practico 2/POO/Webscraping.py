from Api import Api
import pandas as pd

class Webscraping(Api):

  def __init__(self, url, table, tickers):
    '''Crear un dataframe con argumentos de una pagina web y su id de table.'''
    self._url = url
    self._table_id = table
    super().__init__(tickers)

  def _crearDF(self):
    '''Crea dataframe con los atributos guardados.'''
    df = pd.read_html(self._url, attrs=self._table_id, thousands='.', decimal=',', flavor=None)[0]

    df = df.drop(['Efectivo (miles €)', 'Hora'], axis=1)

    columnsName = ["Accion", "Cierre", "Diferencia", "Maximo", "Minimo", "Volumen", "Fecha"]
    df.columns = columnsName

    df_list = list()

    for ticker in self._tickers:

      resultado = df.where(df.Accion == ticker)
      resultado = resultado.dropna()
      df_list.append(resultado)

    df = pd.concat(df_list)

    return df.reset_index()