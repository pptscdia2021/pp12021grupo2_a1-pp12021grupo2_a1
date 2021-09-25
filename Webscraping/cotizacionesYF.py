!pip install yfinance
import yfinance as yf
import pandas as pd

def cotizaciones_yf(tickers, fecha_inicio, fecha_final):
  df = yf.download(tickers, start=fecha_inicio, end=fecha_final,group_by="ticker")
  return df