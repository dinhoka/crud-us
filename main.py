import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, idade INTEGER, cpf TEXT)')
conn.commit()
conn.close()
