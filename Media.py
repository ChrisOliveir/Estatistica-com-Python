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


media_fulano = (8 + 10 + 4+ 8+ 6 + 10+ 8) / 7
print(media_fulano)
print(df['Fulano'].mean()) # formula para média
print(dados.groupby(['Sexo'])['Renda'].mean()) #calcula a média da renda por sexo.

dataset = pd.DataFrame({
    'Sexo': ['H', 'M', 'M', 'M', 'M', 'H', 'H', 'H', 'M', 'M'],
    'Idade': [53, 72, 54, 27, 30, 40, 58, 32, 44, 51]
})

print(dataset.groupby('Sexo').mean().loc['H']) #média apenas dos homens.