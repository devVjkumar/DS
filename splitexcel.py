
# coding: utf-8

# In[1]:


from xlutils.copy import copy
from xlrd import *


# In[15]:


import pandas as pd
name = input("fileName with extension")


# In[24]:


data = pd.read_excel(name, sheetname = 0)
total_rows = len(data.index)


# In[27]:


# total_rows


# In[26]:


# data


# In[31]:


get_split_row = int(input("input"))
start_row = 0
end_row = get_split_row
sheet = 0
flag = 0
while True:
    sheet_name = name + str(sheet) + '.xls'
    writer = pd.ExcelWriter(sheet_name)
#     print(data[start_row:end_row])
    data[start_row:end_row].to_excel(writer,'Sheet1')
    start_row = start_row + get_split_row
    end_row = end_row + get_split_row
    
    writer.save()
    sheet = sheet + 1
    if flag == 1:
        break
    if end_row > total_rows:
        flag = 1
        continue

