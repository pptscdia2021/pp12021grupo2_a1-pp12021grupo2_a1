from Api import Api
import investpy
import pandas as pd

class Investpy(Api):

  def __init__(self, tickers):
    '''Crear dataframe usando API de investing con una cadena de tickers'''
    super().__init__(tickers)
    self._country = 'spain'
    self._df = self._crearDF()

  def _crearDF(self):
    listatickers = list()
    for ticker in self._tickers:
      data = pd.DataFrame(investpy.stocks.get_stock_recent_data(stock=ticker, country=self._country)).tail(1)
      data['Ticker'] = ticker.upper()
      listatickers.append(data)
    df = pd.concat(listatickers) 
    df = df.reset_index()
    columnsName = ["Fecha", "Abierto", "Maximo", "Minimo", "Cierre", "Volumen", "Moneda", "Accion"]
    df.columns = columnsName
    return df