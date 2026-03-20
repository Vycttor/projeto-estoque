import sqlite3

conn = sqlite3.connect('database.db')
conn.execute('''
CREATE TABLE IF NOT EXISTS produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    codigo TEXT NOT NULL,
    fornecedor TEXT NOT NULL,   
    quantidade INTEGER NOT NULL,
    estoque_minimo INTEGER NOT NULL,
    preco REAL NOT NULL,
    data_cadastro DATE NOT NULL
)
''')
conn.close()