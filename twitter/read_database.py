import sqlite3
conn = sqlite3.connect('twitter.db')
cur = conn.cursor()
cur.execute('SELECT * FROM Twitter')
count = 0
for row in cur:
    print row
    count += 1
print count, 'rows.'
cur.close()