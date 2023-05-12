import pandas as pd
import numpy
import matplotlib

dados = pd.read_csv("dados.csv")
print(dados)

#DEFININDO O INTERVALO DAS CLASSES EM REAIS 
classes = [dados.Renda.min(),
           2 * 788,
           5* 788,
           15 * 788,
           25* 788,
           dados.Renda.max()]

print(classes)

df_classes = pd.DataFrame(classes)
label = ('E', 'D', 'C', 'B', 'A')

frequencia = pd.value_counts(
    pd.cut(
    x = dados.Renda,
    bins = classes,
    labels=label,
    include_lowest= True
    )
)
print(frequencia)