from POO_webscrapin import webscraping as ws
from POO_yFinance import yFinance as yf
from POO_investpy import investPy as inv
import pandas as pd

if __name__ == "__main__":
  url = "https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000"
  table = {"id":"ctl00_Contenido_tblAcciones"}
  bolsaMadrid = ws(url, table)

  tickers='BBVA B.SANTANDER TELEFONICA'
  tickers_yF='BBVA.MC SAN.MC TEF.MC'
  tickers_inv = 'bbva san tef'

  yfinance = yf(tickers_yF)
  invpy = inv(tickers_inv)
  bolsaMadrid.toDF()
  yfinance.toDF()
  invpy.toDF()

  bolsaMadrid.toCSV()
  yfinance.toCSV()
  invpy.toCSV()

  ## BOLSA DE MADRID 
  print("\n\nMaxima ganancia y  Maxima pérdida del dia en Bolsa de Madrid:")
  ## Maxima ganancia del dia
  print(bolsaMadrid.maximos("Maximo", 3))
  ## Maxima perdida del dia
  print(bolsaMadrid.minimos("Minimo", 3))


  ## BOLSA DE YFINANCE
  print("\n\nMaxima ganancia y  Maxima pérdida del dia en YFINANCE:")
  ## Maxima ganancia del dia
  print(yfinance.maximos("Maximo", 3))
  ## Maxima perdida del dia
  print(yfinance.minimos("Minimo", 3))

  ## BOLSA DE INVESTPY
  print("\n\nMaxima ganancia y  Maxima pérdida del dia en InvestPY:")
  ## Maxima ganancia del dia
  print(invpy.maximos("Maximo", 3))
  ## Maxima perdida del dia
  print(invpy.minimos("Minimo", 3))
  
