from xlutils.copy import copy
from xlrd import *

import pandas as pd

name = "SET1.xls"
w = copy(open_workbook('grp1.xlsx'))
w_write = w.get_sheet(0)


def findmax(a):
    max = a.max()
    #print(max)
    return a.append(max, ignore_index=True)
	
	
	
	
	
for i in range(64):
    df = pd.read_excel(name, sheetname = i )
    data = df.tail(12).drop([270,273]).T.drop('Unnamed: 10')
    #print(type(data))
    data = abs(data)
    data = findmax(data)
    #max = data.max()
    #print(max)
    #data.append(max, ignore_index=True)
    #print(data)
    if i == 0:
        data1 = data
    else:
        data1 = data1.append(data)
data1





writer = pd.ExcelWriter('output.xls')
data1.to_excel(writer,'Sheet1')
writer.save()





