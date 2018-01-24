import pandas as pd 

#df = pd.read_excel('SET4.xlsx',sheetname = 61)
#k=7
#print(max(df.iloc[1:257,k]))

#print(max(df.iloc[2:258,k]))
#for i in range(0,64):
#	df = pd.read_excel('SET1.xlsx',sheetname = i)
#	print(df.iloc[279:281,:5])
from xlutils.copy import copy
from xlrd import *

w= copy (open_workbook('SET1.xlsx'))
w_write = w.get_sheet(63)
df = pd.read_excel('SET1.xlsx',sheetname = 63)
print(df.iloc[279,1])
w_write.write(280,1,24.1)
w.save('SET1.xlsx')
#print(df.iloc[:,1])

print(abs((df.iloc[1, 0])-( df.iloc[1+1, 0])))

