from openpyxl import load_workbook
from configparser import ConfigParser
import pyodbc

#CONFIGURE
parser = ConfigParser()
parser.read_file(open("conf.ini"))
FileLoad = parser['Config']['FileLoad']
ParametrsCell = parser['Parametrs']['cell']
#ParametrsRow = parser.getint('Parametrs', 'Row')
#ParametrsColumn = parser.getint('Parametrs', 'Column')
print(ParametrsCell)
#print(ParametrsColumn)
#print(ParametrsRow)



#WORK EXCEL

wb = load_workbook(FileLoad)
ws = wb.active
#ws['A1'] = 24

#print(wb.get_sheet_names())

#sheet = wb.get_sheet_by_name('Лист1')
#print(sheet.cell(row=ParametrsRow, column=ParametrsColumn).value)

#sheet = wb.get_sheet_by_name('Лист2')
#print(sheet.cell(row=ParametrsRow, column=ParametrsColumn).value)

wb.save(FileLoad)