from datetime import datetime
import sqlite3

# Функция добавления задачи
def add():
    # Подключение к базе данных
    conn = sqlite3.connect('activitys.db')
    cur = conn.cursor()

    print("Запишите, какую задачу вы хотите добавить:")
    text_activity = input()

    # Получение данных из бд
    cur.execute("SELECT * FROM activitys;")
    all_results = cur.fetchall()

    # Переменная с id задачи
    num = len(all_results) + 1

    # Переменная с датой создания задачи
    date = str(datetime.now())[:16]

    # Сохранине в бд. P.S. Можно было бы сделать обработчик ошибок
    cur.execute(f"""INSERT INTO activitys(id, activity, date) 
    VALUES('{num}.', '{text_activity}', '{date}');""")
    conn.commit()

    print('Задача успешно добавлена!')