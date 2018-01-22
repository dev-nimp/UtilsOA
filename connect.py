import pyodbc
from configparser import ConfigParser

parser = ConfigParser()
parser.read_file(open("conf.ini"))

DriverConnect = parser['Connect']['DRIVER']
ServerConnect = parser['Connect']['SERVER']
DatabaseConnect = parser['Connect']['DATABASE']
UidConnect = parser['Connect']['UID']
PwdConnect = parser['Connect']['PWD']

#connectString = '\'DRIVER={SQL Server}' + ';SERVER=' + ServerConnect + ';DATABASE=' + DatabaseConnect + ';UID=' + UidConnect + ';PWD=' + PwdConnect + '\''
connectString = '\'DRIVER={SQL Server};SERVER=DELOWEB-SERVER\SQLTEST;DATABASE=DBTEST;UID=sa;PWD=1Nz3Z88Lc\''
print(connectString)

cnxn = pyodbc.connect(
    r'DRIVER={SQL Server};'
    r'SERVER=DELOWEB-SERVER\SQLTEST;'
    r'DATABASE=DBTEST;'
    r'UID=sa;'
    r'PWD=1Nz3Z88Lc'
)

#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-4C23489\SQLEXPRESS;DATABASE=DBTEST;UID=admin;PWD=421744Tz')
#cnxn = pyodbc.connect(connectString)

cursor = cnxn.cursor()
#cursor.execute("INSERT dbo.AbUser (user) values ('111')")
cursor.execute("SELECT * FROM dbo.AbUser")
row = cursor.fetchone()
#print(row[0] + row[1])
print(row[1])
#while row:
#    print(str(row[0]+row[1]))
#    row = cursor.fetchone()
#cnxn.commit()
