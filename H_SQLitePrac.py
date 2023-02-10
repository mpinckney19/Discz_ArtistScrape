#Program used when learning the basics of SQLite

import sqlite3

conn = sqlite3.connect('MyFirst.db')
c = conn.cursor()

try:
    c.execute('''CREATE TABLE meals(sandwich TEXT, fruit TEXT, tablenumber INT)''')
except:
    pass

#c.execute('''DROP TABLE meals''')

sandwich = 'chicken'
fruit = 'orange'
tablenum = 22

c.execute('''INSERT INTO meals VALUES(?,?,?)''',(sandwich, fruit, tablenum))
conn.commit()

c.execute('''SELECT * FROM meals''')
results = c.fetchall()

print(results)