import sqlite3
from datetime import datetime
from add_activitys import add
from read_database import read_activitys
from delete_activity import delete
from Write_details import Write
from Read_details import Read
from update_activitys import update
from update_details import update_d


""" >>> Этот файл надо запускать!
     БД - база данных
     После запуска файла команды можно узнать написав 'Помощь'
"""

# Функция, описывающая работу программы
def start():

    # Здесь вызывается функция, для вывода базы данных в консоль, из файла "read_database"
    read_activitys()

    print('Дароу! Це мой трекер задач. В этом меню ты можешь выбрать, что сделать.(Команды есть в меню "Помощь")')

    a = input()

    # Здесь условия, для определения того, что хочет пользователь от программы.
    # Грубо говоря, считывание команд
    if a == 'Добавить описание':
        Write()

    elif a == 'Посмотреть описание':
        Read()

    elif a == 'Добавить задачу':
        add()

    elif a == 'Удалить задачу':
        delete()

    elif a == 'Изменить задачу':
        update()

    elif a == 'Изменить описание':
        update_d()

    elif a == 'Закрыть':
        return a / 0

    elif a == 'Помощь':
        print('Доступные команды: Добавить задачу, Удалить задачу, Добавить описание, Посмотреть описание, Изменить задачу, Закрыть.')

    else:
        print('Что-то пошло не по плану, попробуйте снова <3')

# Здесь запуск функции главной функции, которая обернута в цикл, для того, чтобы программа
# каждый раз не закрывалась, а только тогда, когда этого хочет пользователь.
# Что такое "if __name__ == '__main__'" можешь почитать в инете. В теории это условие должно быть и в
# других модулях, но мне пофиг
if __name__ == '__main__':

    # Здесь код для создания баз данных. Он закоментирован, так как базы данных уже созданы.

    # conn = sqlite3.connect('details.db')
    # cur = conn.cursor()
    #
    # cur.execute("""CREATE TABLE IF NOT EXISTS details(
    #     id TEXT,
    #     detail TEXT)
    #     """)
    # conn.commit()

    #conn = sqlite3.connect('activitys.db')
    #cur = conn.cursor()

    #cur.execute("""CREATE TABLE IF NOT EXISTS activitys(
    #id TEXT,
    #activity TEXT,
    #date TEXT);
    #""")
    #conn.commit()

    while True:
        try:
            start()
        except:
            break