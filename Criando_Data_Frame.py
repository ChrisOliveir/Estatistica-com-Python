import pandas as pd

#CONSTRUINDO A PARTIR DE UM DICIONARIO

df1 = pd.DataFrame({'col1': [1,2], # --> OBS: Se eu não o dicionario ['indice1, indice2] meu index no dataframe seria 0 e 1
                   'col2': [3,4]},
                  ['indice1',
                   'indice2'])

print(df1)

#CONSTRUINDO A APRTIR DE UMNA LISTA DE LISTAS

data = [['tom', 10], ['nick', 15], ['juli', 14]]

df2 = pd.DataFrame(data, columns=['Nome', 'Idade'])
print( df2)

# Criando DataFrame de um dicionário de array/listas

dicionário = {
    'Nome': ['Tom', 'nick', 'krish', 'jack'],
    'Idade': [20, 21, 19, 18],
    'Cor':['branca', 'negra','branca','parda']
}

df3 = pd.DataFrame(dicionário)
print(df3)
