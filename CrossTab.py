import pandas as pd
import numpy 
import seaborn
import scipy

dados = pd.read_csv('dados.csv')

frquencia = pd.crosstab(dados.Sexo, dados.Cor, aggfunc='mean', values= dados.Renda) # aggfunc função agregadora

print(frquencia)

