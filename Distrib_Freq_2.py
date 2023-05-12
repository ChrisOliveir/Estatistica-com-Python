import pandas as pd
import numpy 
import seaborn
import scipy

# DISTRIBUIÇÃO DE FREQUÊNCIAS PARA VARIÁVEIS QUANTITATIVAS
'''
A = ACIMA DE 20 SALARIOS MINIMOS - ACIMA DE 15.760
B = DE 10 A 20 SM DE 7.880 A 15.780
C= DE 4 A 10 SM 3.152 A 7.880
D = DE 2 A 4 SM 1.576 A 3.152
E= ATÉ 2 SM ATÉ 1.576 

'''
dados = pd.read_csv('dados.csv')

print(dados.Renda.min())
print(dados.Renda.max())

classes = [0, 1576, 3152, 7880, 15760, 200000]
labels = ['E', 'D', 'C', 'B','A']

# A pandas.cut() função pode distribuir os dados fornecidos em intervalos, também chamados de bins
distribuicao = pd.value_counts(pd.cut(x= dados.Renda, bins= classes , labels= labels, include_lowest=True))
distribuicao.sort_index(ascending=False, inplace= True)
print(distribuicao)