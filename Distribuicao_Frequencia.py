import pandas as pd
import numpy 
import seaborn
import scipy

dados = pd.read_csv('dados.csv')

# DISTRIBUIÇÃO DE FREQUÊNCIA PARA VARIÁVEIS QUALITATIVAS

print(dados['Sexo'].value_counts())
print(dados['Sexo'].value_counts(normalize=True)* 100) 

frequencia = dados['Sexo'].value_counts()
percentual = dados['Sexo'].value_counts(normalize=True)* 100

distr_freque_qualitatitva = pd.DataFrame({'Frequencia': frequencia, 'Porcentagem(%)': percentual})
#print(distr_freque_qualitatitva)
distr_freque_qualitatitva.rename(index= {0: 'Masculino', 1: 'Feminino'}, inplace= True) #Inplace = True significa que o quadro de dados deve tornar as alterações permanentes

distr_freque_qualitatitva.rename_axis('Sexo', axis = 'columns', inplace=True)
print(distr_freque_qualitatitva)

sexo = {0: 'Masculino', 1:'Feminino'}
cor = {0: 'Indigena',
       2: 'Branca',
       4: 'Preta',
       6: 'Amarela',
       8: 'Parda',
       9: 'Sem declaração'

}
frequencia = pd.crosstab(dados.Sexo, dados.Cor) #(index, columns)
frequencia.rename(index=sexo, inplace=True)
frequencia.rename(columns= cor, inplace= True)
print(frequencia)