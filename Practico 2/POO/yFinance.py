from Api import Api
import yfinance as yf
import pandas as pd

class yFinance(Api):    

  def _crearDF(self):
    listatickers = list()
    for ticker in self._tickers:
      data = yf.download(ticker, group_by="ticker", period='1d')
      data['Ticker'] = ticker
      listatickers.append(data)
    df = pd.concat(listatickers)
    column = df['Ticker']
    del(df['Ticker'])
    df.insert(0, 'Ticker', column)
    df = df.reset_index()
    columnsName = ["Fecha", "Accion", "Abierto", "Maximo", "Minimo", "Cierre", "Volumen"]
    df = df.drop(['Adj Close'], axis=1)
    df.columns = columnsName
    return df