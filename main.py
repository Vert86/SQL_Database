from sql import connect, cursor

cursor.execute("select * from 'ips'")
main_data = cursor.fetchall()

print(main_data)