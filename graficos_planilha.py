#!./env/bin/python
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

xls = pd.ExcelFile("Ficha de Monitoramento e Avaliação dos PMEs 2018_final.xls")
#print(xls.sheet_names)




df1 = pd.read_excel(xls,'Meta 1')
#print(df1.loc[14][5])

years= [ x for x in df1.loc[13][3:15]]
#------- indicador 1A ------#
meta_prevista_1A =[ x for x in df1.loc[14][3:15]]
meta_executada_1A =[ x for x in df1.loc[15][3:15]]

print(years[2])
