import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Добавляем нового пользователя
cursor.execute('INSERT INTO Users (username, email, age) VALUES (?, ?, ?)', (
    'Вася', 'newuser@example.com', 55))

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()