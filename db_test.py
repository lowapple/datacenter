import config

conn = config.connectMySQL()
curs = conn.cursor()
# curs.execute('CREATE DATABASE dbTest;')
curs.execute('''
CREATE TABLE users (
        id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        name varchar(255) NOT NULL );''')

curs.execute('INSERT INTO users (name) VALUES (%s);', ('Hello World'))
conn.commit()
conn.close()