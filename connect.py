import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-4C23489\SQLEXPRESS;DATABASE=DBTEST;UID=admin;PWD=421744Tz')

cursor = cnxn.cursor()
#cursor.execute("INSERT INTO dbo.AbUser (user) values ('111')")
cursor.execute("SELECT * FROM dbo.AbUser")
row = cursor.fetchone()
while row:
    print(str(row[0]))
    row = cursor.fetchone()

#cnxn.commit()
