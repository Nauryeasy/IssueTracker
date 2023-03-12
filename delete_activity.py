import sqlite3

# Функция удаления задач из бд


def delete():

    # Снова подключение к бд
    conn = sqlite3.connect('activitys.db')
    cur = conn.cursor()

    print('Задачу под каким id вы желаете удалить?')

    id = input()

    # Удаления поля в бд, где id совпадает с указанным пользователем
    cur.execute(f"DELETE FROM activitys WHERE id='{id}.';")
    conn.commit()

    # Получение всех записей из бд
    cur.execute("SELECT * FROM activitys;")
    all_results = cur.fetchall()

    # Обработчик ошибок, в котором редактируется айди задач
    # Пример:
    # 1. Попить
    # 2. Поесть
    # >>>
    # Если удаляем первую, задачу, то вторая должна стать первой. Это тут и происходит
    # P.S. Зачем обработчик ошибок, я хз. Наверное, когда тестил, не работало что-то
    try:
        # Проверяем, не является ли задача последней
        if int(id) != int(all_results[-1][0][0]):
            # Проходимся циклом и меняем айди
            for i in range(int(id)+1, int(all_results[-1][0][0]) + 1):
                cur.execute(f"UPDATE activitys SET id='{i-1}.' where id = '{i}.'")
                conn.commit()
    except:
        pass

    # Подключаемся к бд с описанием к задачам
    conn = sqlite3.connect('details.db')
    cur = conn.cursor()

    # Удаляем описание к задаче, с указаным пользователем айди
    cur.execute(f"DELETE FROM details WHERE id='{id}.';")
    conn.commit()

    cur.execute("SELECT * FROM details;")
    all_results = cur.fetchall()

    # Тут та же самая махинация с айди, что и была выше
    try:
        if int(id) != int(all_results[-1][0][0]):
            for i in range(int(id)+1, int(all_results[-1][0][0]) + 1):
                cur.execute(f"UPDATE details SET id='{i-1}.' where id = '{i}.'")
                conn.commit()
    except:
        pass

    print('Задача успешно удалена!')