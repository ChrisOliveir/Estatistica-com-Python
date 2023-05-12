''' MEDIANA É O VALOR QUE DIVIDE A SERIE EXATAMENTE AO MEIO 
[ 6, 4, 3, 9, 1] DESORDENADO
[1, 3, 4, 6, 9] ORDENADO N+1/2 ONDE N É O NUMERO DE AMOSTRAS 
6 + 1 / 2 = 3
3 É A MEDIANA
'''
import pandas as pd 

dados = pd.read_csv('dados.csv')

df = pd.DataFrame(data = {'Fulano': [8, 10, 4, 8, 6, 10, 8],
                  'Beltrano': [10, 2,0.5, 1, 3, 9.5, 10],
                  'Sicrano':[7.5, 8, 7, 8, 8, 8.5, 7]},

                  index = ['matematica',
                          'portugues',
                          'ingles',
                          'geografia',
                          'historia',''
                          'fisica',
                          'quimica'])

df.rename_axis('Materias', axis='columns', inplace=True)

notas_fulano = df.Fulano
notas_fulano = notas_fulano.sort_values()
n = notas_fulano.shape[0]
print(notas_fulano.median())