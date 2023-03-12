import sqlite3

# Функция обновления задачи


def update():

    # Подключение к бд
    conn = sqlite3.connect('activitys.db')
    cur = conn.cursor()

    # Получение инфы из бд
    cur.execute("SELECT * FROM activitys;")
    all_results = cur.fetchall()

    # Проверка, не пустая ли бд
    if all_results:
        x = 0

        print('Напишите id задачи, которую хотите изменить:')
        id = input()

        for activity in all_results:

            if activity.count(id + '.') > 0:
                x = 1

        if x == 1:

            print('Напишите новый текст задачи:')
            text = input()

            cur.execute(f"UPDATE activitys SET activity='{text}' WHERE id='{id}.'")

            conn.commit()

            print('Задача успешно обновлена!')
            # except:
            #     print('Произошла непредвиденная ошибка')
        else:
            print('Нет задачи с таким id!')