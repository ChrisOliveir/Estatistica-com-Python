# É A REPRESENTAÇÃO GRÁFICA DE UMA DISTRIBUIÇÃO DE FREQUÊNCIAS.

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('dados.csv')
plt.hist(dados.Altura, bins=30)
#plt.hist(dados.query('Renda < 20000').Renda,  bins =30)
plt.show()