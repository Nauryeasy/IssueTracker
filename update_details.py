import sqlite3

# Функция обновления описания к задачам
# Комментариев нет, так как тут везде все тоже самое


def update_d():
    conn = sqlite3.connect('activitys.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM activitys;")
    all_results = cur.fetchall()

    if all_results:
        x = 0

        print('Напишите id задачи, описание которой хотите изменить:')
        id = input()

        for activity in all_results:

            if activity.count(id + '.') > 0:
                x = 1

        if x == 1:

            print('Напишите новый текст описания:')
            text = input()

            conn = sqlite3.connect('details.db')
            cur = conn.cursor()

            cur.execute(f"UPDATE details SET detail='{text}' WHERE id='{id}.'")

            conn.commit()

            print('Описание успешно обновлена!')
            # except:
            #     print('Произошла непредвиденная ошибка')
        else:
            print('Нет задачи с таким id!')