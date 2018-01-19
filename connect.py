import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DELOWEB-SERVER\SQLTEST;DATABASE=DBTEST;UID=sa;PWD=1Nz3Z88Lc')

cursor = cnxn.cursor()
cursor.execute("INSERT INTO AbUser(user) values ('111')")
cnxn.commit()