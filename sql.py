import sqlite3

connect = sqlite3.connect('database.db')
cursor = connect.cursor()

cursor.execute("select * from 'ips'")
fetch_data01 = cursor.fetchall()
#print(fetch_data01)

cursor.execute("select domain from 'ips' ORDER BY asn desc")
fetch_data02 = cursor.fetchall()
#print(fetch_data02)

cursor.execute("select address, domain from 'ips' WHERE domain like '%patri%' or domain like '%devo%'")
fetch_data03 = cursor.fetchall()
#print(fetch_data03)

