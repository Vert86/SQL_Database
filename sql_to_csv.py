from sql import connect, cursor
import pandas


df = pandas.read_sql_query("SELECT * FROM 'ips'", connect)
#print(df)

df.to_csv('database.csv', index=None)
#df.to_excel('database.xlsx', index=None)