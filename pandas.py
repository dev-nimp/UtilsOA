import pandas
from openpyxl import load_workbook

book = load_workbook('empty_book.xlsx')
writer = pandas.ExcelWriter('empty_book.xlsx', engine='openpyxl')
writer.book = book
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

data_filtered.to_excel(writer, "Main", cols = ['Diff1', 'Diff2'])

writer.save()