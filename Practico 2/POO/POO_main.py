from POO_webscrapin import webscraping as ws
from POO_yFinance import yFinance as yf
from POO_investpy import investPy as inv
from POO_graficos import Graficos as gf
import pandas as pd

if __name__ == "__main__":
  url = "https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000"
  table = {"id":"ctl00_Contenido_tblAcciones"}
  tickers = 'BBVA TELEFONICA B.SANTANDER'

  tickers2 = 'bbva.mc tef.mc san.mc'
  data_yf = yf(tickers2.upper())
  data2 = data_yf.toDF()
  data_yf.toCSV()
  prin('----{0}----'.format('yFinance'))
  print(data_yf.maximos('Maximo', 3))
  print(data_yf.minimos('Minimo', 3))

  data_inv = inv(tickers2.replace('.mc', ''))
  data3 = data_inv.toDF()
  data_inv.toCSV()
  prin('----{0}----'.format('InvestPy'))
  print(data_inv.maximos('Maximo', 3))
  print(data_inv.minimos('Minimo', 3))

  webscrap = ws(url, table, tickers)
  data = webscrap.toDF()
  prin('----{0}----'.format('Webscrapin'))
  print(webscrap.maximos('Maximo', 3))
  print(webscrap.minimos('Minimo', 3))
  webscrap.toCSV()

  df_dict = {'Webscraping':data, 'yFinance':data2, 'InvestPy':data3}
  grafic = gf(df_dict)
  grafic.dibujar(12)