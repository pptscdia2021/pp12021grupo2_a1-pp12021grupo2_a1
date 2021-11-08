from POO_webscrapin import webscraping as ws
from POO_yFinance import yFinance as yf
from POO_investpy import investPy as inv
from POO_graficos import Graficos as gf
import pandas as pd

if __name__ == "__main__":
  url = "https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000"
  table = {"id":"ctl00_Contenido_tblAcciones"}
  bolsaMadrid = ws(url, table)

  webscrap = ws(url, table)
  data = webscrap.toDF()
  webscrap.maximos('Maximo', 3)
  webscrap.toCSV()


  tickers = 'BBVA TELEFONICA B.SANTANDER'
  df_list = list()
  for ticker in list(tickers.split()):
    resultado = data.where(data.Accion == ticker)
    resultado = resultado.dropna()
    df_list.append(resultado)

  data = pd.concat(df_list)

  tickers2 = 'bbva.mc tef.mc san.mc'
  data_yf = yf(tickers2.upper())
  data2 = data_yf.toDF()
  data_yf.toCSV()
  data_yf.maximos('Maximo', 3)

  data_inv = inv(tickers2.replace('.mc', ''))
  data3 = data_inv.toDF()
  data_inv.toCSV()
  data_inv.maximos('Maximo', 3)

  df_dict = {'Webscraping':data, 'yFinance':data2, 'InvestPy':data3}
  grafic = gf(df_dict)
  grafic.dibujar(12)