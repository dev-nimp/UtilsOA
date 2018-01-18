#import configparser
from openpyxl import load_workbook
from configparser import ConfigParser


#PARSER
parser = ConfigParser()
parser.read_file(open("conf.ini"))

FileLoad = parser['Config']['FileLoad']
ParametrsRow = parser.getint('Parametrs', 'Row')
ParametrsColumn = parser.getint('Parametrs', 'Column')


#print(ParametrsColumn)
#print(ParametrsRow)

#WORK EXCEL

wb = load_workbook(FileLoad)
ws = wb.active
ws['A1'] = 2

#print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('Лист1')
print(sheet.cell(row=ParametrsRow, column=ParametrsColumn).value)

sheet = wb.get_sheet_by_name('Лист2')
print(sheet.cell(row=ParametrsRow, column=ParametrsColumn).value)

wb.save(FileLoad)