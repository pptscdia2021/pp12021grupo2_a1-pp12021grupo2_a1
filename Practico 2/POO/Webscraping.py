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

    df, = pd.read_html(self._url, attrs=self._table_id, thousands='.', decimal=',', flavor=None)

    df = df.drop(['Efectivo (miles €)', 'Hora'], axis=1)

    df.columns = ["Accion", "Cierre", "Diferencia", "Maximo", "Minimo", "Volumen", "Fecha"]

    df = df[df.Accion.isin(self._tickers)]

    return df.reset_index()