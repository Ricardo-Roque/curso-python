import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read   Update Delete 
# SQL -  INSERT SELECT UPDATE DELETE 

# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(:nome, :peso)'
)

# Registrar valores nas colunas da tabela
# cursor.execute(sql, ['Joana', 4])
# cursor.executemany(
#     sql, 
#     (
#         ('Joana', 4), ('Luis', 4)
#     )
# )

cursor.execute(sql, {'nome':'Joana', 'peso':4})
cursor.executemany(
    sql, 
    (
        {'nome':'Joana', 'peso':4},
        {'nome':'Miano', 'peso':4},
        {'nome':'Maria', 'peso':4},
        {'nome':'Amanda', 'peso':4},
    )
)
connection.commit()

if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="QUALQUER VALOR"'
        'WHERE id = 2'
    )
    connection.commit()

    cursor.execute(
        f'SELECT * FROM {TABLE_NAME}'
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()