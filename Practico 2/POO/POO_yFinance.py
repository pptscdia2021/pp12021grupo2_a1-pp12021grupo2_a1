import yfinance as yf
import pandas as pd

class yFinance:    
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
      self.tickers = self.tickers.reset_index()
      columnsName = ["Fecha", "Accion", "Abierto", "Maximo", "Minimo", "Cierre", "Volumen"]
      self.tickers = self.tickers.drop(['Adj Close'], axis=1)
      self.tickers.columns = columnsName

    def cotizaciones(self):
      return self.tickers

    def toCSV(self):
      return self.tickers.to_csv('yFinance.csv')

    def maximos(self, columna, cantidad):
        '''Devuelve la cantidad de maximos indicado del DataFrame indicando la columna'''
        resultado = self.tickers.sort_values(columna, ascending=False)
        resultado = resultado.head(cantidad).to_dict('records')
        resultado = list(map(lambda x: 'Ganancia maxima del día de {0}: {1}'.format(x['Accion'], x[columna]), resultado))
        return '\n'.join(resultado)

    def minimos(self, columna, cantidad):
      '''Devuelve la cantidad de minimos indicado del DataFrame indicando la columna'''
      resultado = self.tickers.sort_values(columna)
      resultado = resultado.head(cantidad).to_dict('records')
      resultado = list(map(lambda x: 'Mayor perdida del día de {0}: {1}'.format(x['Accion'], x[columna]), resultado))
      return '\n'.join(resultado)        
