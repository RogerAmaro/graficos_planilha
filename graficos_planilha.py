#!./env/bin/python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce

xls = pd.ExcelFile("Ficha de Monitoramento e Avaliação dos PMEs 2018_final.xls")
#print(xls.sheet_names)




df1 = pd.read_excel(xls,'Meta 1')
#print(df1.loc[14][5])

years= [ x for x in df1.loc[13][3:15]]
#------- indicador 1A ------#
# meta_prevista_1A =[ x for x in df1.loc[14][3:15]]
meta_prevista_1A = [x for x in df1.loc[14][3:15]]
for i in meta_prevista_1A:
    if np.isnan(i):
        meta_prevista_1A[meta_prevista_1A.index(i)]=0
        
meta_executada_1A =[ x for x in df1.loc[15][3:15]]
for i in meta_executada_1A:
    if np.isnan(i):
        meta_executada_1A[meta_executada_1A.index(i)]=0

meta_executada_1A = [ x*100 for x in meta_executada_1A]
meta_prevista_1A = [ x*100 for x in meta_prevista_1A]



width = 0.2
labels = [ str(x) for x in years]
ind = np.arange(len(labels))

bar_prevista = plt.bar(ind + width,meta_prevista_1A, width, color='g', label='Meta prevista')
bar_executada = plt.bar(ind,meta_executada_1A, width, color='r', label='Meta Executada')

fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)



location = ind+width/2
labels=labels
plt.xticks(location, labels)

plt.legend()
plt.grid()
plt.ylabel("Execução ( em %)")
plt.xlabel("Ano")
fig.savefig('test2png.png', dpi=100)
plt.show()