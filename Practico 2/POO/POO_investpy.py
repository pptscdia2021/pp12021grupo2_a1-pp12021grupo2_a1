import investpy
import pandas as pd

class Investpy:
  def __init__(self, stocks):
     self.country = 'spain'
     self.as_json= True
     self.order = 'ascending'
     self.interval = 'Daily'
     self.stocks = list(stocks.split())

     listatickers = list()
     for ticker in self.stocks:
       data = pd.DataFrame(investpy.stocks.get_stock_recent_data(stock=ticker, country=self.country)).tail(1)
       data['Ticker'] = ticker.upper()
       listatickers.append(data)
     self.df = pd.concat(listatickers) 
     self.df = self.df.reset_index()
     columnsName = ["Fecha", "Abierto", "Maximo", "Minimo", "Cierre", "Volumen", "Moneda", "Accion"]
     self.df.columns = columnsName

  def toDF(self):
    return self.df

  def toCSV(self):
    return self.df.to_csv('investypy.csv')

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
