from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class Graficos:

  def __init__(self, df_dict):
    self.df = df_dict
    self.params = {'Maximos':{'df':'Maximo', 'colors':['#34BE82', '#2F86A6', '#2FDD92'], 'colum':0},
                    'Minimos':{'df':'Minimo', 'colors':['#FF0000', '#950101', '#3D0000'], 'colum':1}}
  
  def dibujar(self, size=10):

    fig, ax = plt.subplots(figsize=(size,size), nrows=len(self.df), ncols=2)
    r = 0

    for key, df in self.df.items():

      for param, value in self.params.items():

        for i in df.index:

          ax[r][value['colum']].bar(df.Accion[i], df[value['df']][i], color=value['colors'][i], label=df.Accion[i])

        ax[r][value['colum']].set_title(key.upper() ,fontsize=(size*1.1))
        ax[r][value['colum']].grid()
        ax[r][value['colum']].set_ylabel(param, fontsize=size)
        ax[r][value['colum']].legend()

      r+=1

    plt.tight_layout()
    
    return plt.show()