#import pandas as pd 
#status = pd.read_excel("cse.xls")
#df = pd.DataFrame(status,columns = ['Student Name'])
#df1=max(df[df.columns[9]])
#se = pd.Series(status)
#print(df[-1,0])
import xlsxwriter as xlw 
from xlrd import open_workbook
#from xlutils.copy import copy

#wb = xlw.workbook('cse.xls')
#wb = copy(wb)

#ws = wb.get_sheet(0)
#wb.write(76,8,"65")
#wb.save('cse.xls')
import openpyxl

book = openpyxl.load_workbook('cse.xls')

sheet = book.active

sheet.cell(row = 76, column = 5).value = '52'

