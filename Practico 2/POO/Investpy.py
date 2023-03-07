from Api import Api
import investpy
import pandas as pd

class Investpy(Api):

  def _crearDF(self):

    listatickers = list()

    for ticker in self._tickers:
      data = pd.DataFrame(investpy.stocks.get_stock_recent_data(stock=ticker, country='spain')).tail(1)
      data['Ticker'] = ticker.upper()
      listatickers.append(data)

    df = pd.concat(listatickers) 
    df = df.reset_index()
    df.columns = ["Fecha", "Abierto", "Maximo", "Minimo", "Cierre", "Volumen", "Moneda", "Accion"]

    return df