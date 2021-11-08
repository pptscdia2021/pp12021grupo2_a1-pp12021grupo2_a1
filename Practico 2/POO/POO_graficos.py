from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class Graficos:
  def __init__(self, df_dict):
    ''''Recibe un atributo dict {name:dataFrame} para graficar'''
    self.df = df_dict
  
  def dibujar(self):
    fig, ax = plt.subplots(figsize=(10,10), nrows=len(self.df), ncols=2)
    r = 0
    c = 0
    colors_max = ['#34BE82', '#2F86A6', '#2FDD92']
    colors_min = ['#FF0000', '#950101', '#3D0000']
    color = 0
    for key, df in self.df.items():
      c = 0
      color = 0

      ax[r][c].set_title(key.upper() ,fontsize=12)

      for i in df.index:
        ax[r][c].bar(df.Accion[i], df.Maximo[i], color=colors_max[color], label=df.Accion[i])
        ax[r][c].grid()
        ax[r][c].set_ylabel('Maximos')
        ax[r][c].legend()
        color+=1

      c+=1
      ax[r][c].set_title(key.upper() ,fontsize=12)
      color=0
      for i in df.index:
        ax[r][c].bar(df.Accion[i], df.Minimo[i], color=colors_min[color], label=df.Accion[i])
        ax[r][c].grid()
        ax[r][c].set_ylabel('Minimos',fontsize=10)
        ax[r][c].legend()
        color+=1
      r+=1
    plt.tight_layout()
    
    return plt.show()