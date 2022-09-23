from sql import connect, cursor

new_rows=[
  ('100.100.100.100', 'abd.dcf.hgg', 122),
  ('123,255.243.01', 'hdh.jh.jdhdh', 11)
]
cursor.executemany("INSERT INTO 'ips' VALUES(?,?,?)", new_rows)
connect.commit

cursor.execute("SELECT * FROM 'ips'")
print(cursor.fetchall())
