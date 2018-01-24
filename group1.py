from xlutils.copy import copy
from xlrd import *

import pandas as pd 
#for i in range(1,6):
name = "SET"+str(6)+".xlsx"
w = copy(open_workbook(name))
df = pd.ExcelFile(name)
for j in range(0,64):
    df = pd.read_excel(name, sheetname = j )
    w_write = w.get_sheet(j)
       #df1 = df.parse(j)
       
    for k in range(0,10):
        avg = []
        for l in range(1, 256):
            avg.append(abs((df.iloc[l, k])-( df.iloc[l+1, k])))




        w_write.write(281, k+1, max(avg))
            #max1 = max(df.iloc[2:258,k])
        #if i == 2 or i == 3:
        #    w_write.write(269, k+1, max(avg))
        #else:
        #    w_write.write(281, k+1, max(avg))



#w_write = w.get_sheet(0)
#w_write.write(1,1,vijay)
w.save(name)