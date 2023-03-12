import sqlite3

# Функция чтения и вывода всех задач из бд

def read_activitys():

    # Подключение к базе данных
    conn = sqlite3.connect('activitys.db')
    cur = conn.cursor()

    # Получение всей информации из бд "activitys"
    cur.execute("SELECT * FROM activitys;")
    all_results = cur.fetchall()

    # Вывод данных из базы данных
    if all_results:
        for activity in all_results:
            make = ''
            for i in activity:
                make = make+ ' ' + i
            print(make)
    # Условие на случай, если база данных пустая
    else:
        make = 'На данный момент задач нет >.<'
        print(make)