import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY, 
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER
)
''')
# **INTEGER**: Целые числа.
# **TEXT**: Текстовые данные.
# **REAL**: Числа с плавающей запятой.
# **BLOB**: Двоичные данные.
cursor.execute('''
INSERT INTO Users (id, username, email, age) VALUES (1, 'Иванов', 'be@be.be', 18
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()