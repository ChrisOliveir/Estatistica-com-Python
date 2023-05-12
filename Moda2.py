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
print(df)

print('A moda é {}:'.format(dados.Altura.mode()))
print('A mediana é {}:'.format(dados.Altura.median()))
print('A média é {}:'.format(dados.Altura.mean()))