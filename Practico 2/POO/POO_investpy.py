
import investpy
import pandas as pd

class Investpy:
    def __init__(self, country):
     self.country = country
     self.as_json= False
     self.order = 'ascending'
     self.interval = 'Daily'
     self.df = investpy.stocks.get_stocks_overview(country=self.country, as_json = self.as_json , n_results = 35)
     del(self.df['country'])

    def toDF(self):
        return self.df

ipy = Investpy('spain')
ipy.toDF()


