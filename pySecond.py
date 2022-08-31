print ("Welcome!")
print ("FRom Akansha")
import pyodbc as db
server = 'ak-test-sql-server.database.windows.net'
database = 'AK_DB_SAMPLE'
username = 'rootadmin'
password = '{Sqlserver123}'   
driver= '{ODBC Driver 17 for SQL Server}'
conx = db.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conx.cursor()
cursor.execute("select * from SalesLT.Address")
row = cursor.fetchone()
for row in cursor:
    CITY = row.City
    print(CITY)
conx.commit()

