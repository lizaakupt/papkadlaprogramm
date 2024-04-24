import sqlite3

connect = sqlite3.connect('fructs.sqlite')
cursor = connect.cursor()



cursor.execute('''
CREATE TABLE IF NOT EXISTS Fructs(
 name TEXT,
 color TEXT,
 size TEXT
 )
  ''')

cursor.execute('''
INSERT INTO Fructs (name, color, size) VALUES
 ('apple', 'red', 'большой'),
 ('watermelon', 'pink', 'средний')
  ''')


cursor.execute('''
DELETE FROM Fructs WHERE size = 'большой'
''')
connect.commit()

result = cursor.execute('''
SELECT * FROM Fructs

''')

for i in result.fetchall():
    print(i)



connect.close()