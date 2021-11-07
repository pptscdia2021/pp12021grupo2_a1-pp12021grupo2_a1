import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class yFinance:
    '''def __init__(self,tickers):
        self.tickers = [yf.download(ticker, group_by="ticker", period='1d') for ticker in list(tickers.split())]'''
    
    def __init__(self,tickers):
      self.tickers = pd.DataFrame()
      listatickers = list()
      for ticker in list(tickers.split()):
        data = yf.download(ticker, group_by="ticker", period='1d')
        data['Ticker'] = ticker
        listatickers.append(data)
      self.tickers = pd.concat(listatickers)
      column = self.tickers['Ticker']
      del(self.tickers['Ticker'])
      self.tickers.insert(0, 'Ticker', column)

    def cotizaciones(self):
      return self.tickers


tickers = 'BBVA.MC SAN.MC'

df = yf.download(tickers,group_by="ticker", period='1d')
df

prueba = yFinance(tickers)
prueba.cotizaciones()