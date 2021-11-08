from POO_webscrapin import webscraping as ws
from POO_yFinance import yFinance as yf
from POO_investpy import investPy as inv
import pandas as pd

if __name__ == "__main__":
  url = "https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000"
  table = {"id":"ctl00_Contenido_tblAcciones"}
  bolsaMadrid = ws(url, table)

  tickers = 'bbva san tef'
  yfinance = yf(tickers)
  invpy = inv(tickers)
  bolsaMadrid.toDF()
  yfinance.toDF()
  invpy.toDF()

  bolsaMadrid.toCSV()
  yfinance.toCSV()
  invpy.toCSV()
