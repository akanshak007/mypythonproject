import sqlite3

conn = sqlite3.connect('test.db')
print ("db open success")

cursor = conn.execute("SELECT * FROM COMPANY")
row = cursor.fetchmany()
for i in row:
# for row in cursor:

    print ("ID= ", i[0])
    row = cursor.fetchmany()

    # print ("Name= ", row[1])
    # print("Address= ", row[2])
    # print ("Salary= ", row[3])
    # print ("\n")

    print ("Fetch operation success")
    conn.close()