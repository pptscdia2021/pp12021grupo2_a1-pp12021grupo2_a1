#!pip install yfinance
import yfinance as yf
import pandas as pd


def cotizaciones_yf(tickers, fecha_inicio, fecha_final):
  df = yf.download(tickers, start=fecha_inicio, end=fecha_final,group_by="ticker")
  return df


if __name__ == "__main__":
  amzn = cotizaciones_yf("AMZN", "2021-10-03", "2021-10-05")
  amzn.to_csv('Practico 2/Webscraping/csv/amzn.csv', index = False)
  print(amzn)
  ticker = yf.Ticker('YPF')
  amzn_df = ticker.history(period="5y")
  amzn_df['Close'].plot(title="YPF SA stock price")