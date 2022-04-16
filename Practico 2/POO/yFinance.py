from Api import Api
import yfinance as yf
import pandas as pd

class yFinance(Api):    

  def _crearDF(self):

    listatickers = list()

    for ticker in self._tickers:
      data = yf.download(ticker, group_by="ticker", period='1d')
      data.insert(0, 'Ticker', ticker)
      listatickers.append(data)
      
    df = pd.concat(listatickers)
    df = df.reset_index()
    df = df.drop(['Adj Close'], axis=1)
    df.columns = ["Fecha", "Accion", "Abierto", "Maximo", "Minimo", "Cierre", "Volumen"]

    return df