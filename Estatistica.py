import pandas as pd
import numpy 
import seaborn
import scipy

print(pd.__version__)


dados = pd.read_csv('dados.csv')
print(dados.head()) #mostra os 5 primeiros registros

#VARIAVEIS QUALITATIVAS ORDINAIS(Podem ser ordenadas ou hierarquizadas)

print(sorted(dados['Anos de Estudo'].unique())) # unique retorna valores unicos e sorted ordena valores

#VARIAVEIS QUALITATIVAS NOMINAIS (variaveis que não podem ser ordenadas ou hierarquizadas)

print(sorted(dados['UF'].unique()))
print(sorted(dados['Sexo'].unique()))
print(sorted(dados['Cor'].unique()))

# VARIAVEIS QUANTITATIVAS DISCRETAS (Variaveis que representam uma contagem onde os valores possiveis formam um conjunto finito ou enumerável)

print(dados.Idade.min())
print(dados.Idade.max())
print("De {} a {} anos".format(dados.Idade.min(), dados.Idade.max()))

# VARIAVEIS QUANTITATIVAS CONTINUAS (Variaveis que representa uma contagem ou mensuração que assumem valores em uma escala continua de numeros reais

