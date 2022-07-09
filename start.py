import sqlite3

conn = sqlite3.connect('test_database')
c = conn.cursor()

#   Initiate test database for 1 project
c.execute('''
          CREATE TABLE IF NOT EXISTS project
          ([product_id] INTEGER PRIMARY KEY, [nbrCommits24h] INTEGER, [sizeCommits24h] DOUBLE)
          ''')

conn.commit()