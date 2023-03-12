import sqlite3

# >>> Функция для добавления описания к задачам

def Write():
    # Подключение к базе данных
    conn = sqlite3.connect('activitys.db')
    cur = conn.cursor()

    # Получение всей инфы из бд
    cur.execute("SELECT * FROM activitys;")
    all_results = cur.fetchall()

    # Условие, проверяющее пустая ли бд
    if all_results:

        # Что-то типо флага, которая становиться True, если такая задача есть
        x = 0

        print('К какой задаче вы хотите добавить описание?')

        id = input()

        # Поиск задачи по айди

        for activity in all_results:

            if activity.count(id + '.') > 0:
                x = 1

        # Добавление описания к задаче
        if x == 1:

            print('Напишите описание')

            detail = input()

            # Подключение к бд с описаниями к задачам
            conn = sqlite3.connect('details.db')
            cur = conn.cursor()

            # Добавление новой записи
            cur.execute(f"""INSERT INTO details(id, detail) 
                    VALUES('{id}.', '{detail}');""")

            # Сохранение новой записи
            conn.commit()

            print("Описание успешно добавлено!")

        # Если айди задачи не найдено
        else:
            print('Задачи с таким id несуществует')

    # Если нет задач
    else:
        return print('Задач нет')

