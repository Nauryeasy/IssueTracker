import sqlite3

# Функция чтения описания к задаче с указаным айди из бд

def Read():
    print('У какой задачи вы хотите просмотреть описание?')

    id = input()

    # Снова подключаемся к бд(
    conn = sqlite3.connect('details.db')
    cur = conn.cursor()

    # Достаем из бд описание с указаным айди
    cur.execute(f"SELECT * FROM details WHERE id='{id}.'")
    all_results = cur.fetchall()
    make = ''
    if all_results:
        for activity in all_results:
            for i in activity:
                make = make + i + ' '
    else:
        make = 'У данной задачи нет описания'

    print(make)