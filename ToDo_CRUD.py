import requests
import json


key_names = ['id', 'name', 'priority']
key_width = [5, 30, 10]

def show_head():
    '''Функция, отображающая шапку таблицы.'''
    for(n, w) in zip(key_names, key_width):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    '''Функция, добавляющая пробелы в отображении.'''
    for w in key_width:
        print(' '.ljust(w), end='| ')
    print()


def show_task(task):
    '''Функция, отображающая задачу.'''
    for(n, w) in zip(key_names, key_width):
        print(str(task[n]).ljust(w), end='| ')
    print()


def show(json):
    '''
    Функция отображения.
    ____________________
    
    Принимает:
        Данные из хоста.
    Возвращает:
        Если данные являются объектами класса dict или list,
        Отображает данные. Если иначе оставляет пустую строку.
    '''

    show_head()
    if isinstance(json, list):
        for task in json:
            show_task(task)
    elif isinstance(json, dict):
        if json:
            show_task(json)
        else:
            show_empty()


def show_all():
    '''Функция, отображающая все задачи.'''
    try:
        reply = requests.get('http://localhost:3000/tasks')
    except requests.RequestException:
        print('Communication error')
    else:
        if reply.status_code == requests.codes.ok:
            show(reply.json())
        else:
            print('Server error')


def show_one():
    '''Функция, позволяющая отобразить одну задачу на выбор.'''
    what_task_to_see = int(input('Какую задачу вы хотите увидеть? '))
    try:
        reply = requests.get(f'http://localhost:3000/tasks/{what_task_to_see}')
    except requests.RequestException:
        print('Communication error')
    else:
        if reply.status_code == requests.codes.ok:
            show(reply.json())
        else:
            print('Server error')


def sort_tasks_from_small_to_big():
    '''Функция, позволяющая отсортировать задачи по возрастанию приоритета.'''
    try:
        reply = requests.get('http://localhost:3000/tasks/?_sort=priority')  # Тут можно прописать условия отображения.
    except requests.RequestException:
        print('Communication error')
    else:
        if reply.status_code == requests.codes.ok:
            show(reply.json())
        else:
            print('Server error')


def sort_tasks_from_big_to_small():
    '''Функция, позволяющая отсортировать задачи по убыванию приоритета.'''
    try:
        reply = requests.get('http://localhost:3000/tasks/?_sort=priority&_order=desc')  # Сортировка по убыванию приоритета.
    except requests.RequestException:
        print('Communication error')
    else:
        print('Connection=' + reply.headers['Connection'])  # Можно проверять статус подключения.
        if reply.status_code == requests.codes.ok:
            show(reply.json())
        elif reply.status_code == requests.codes.not_found: 
            print('Resourse not found')
        else:
            print('Server error')


def delete_task():
    '''Функция, позволяющая удалить задачу по номеру id.'''
    headers = {'Connection': 'Close'}  # Переменная для закрытия потока.
    id_del = int(input('Какую запись хотите удалить? '))
    try:
        reply = requests.delete(f'http://localhost:3000/tasks/{id_del}')  # Удаляем запись по первому индексу.
        print('res=' + str(reply.status_code))
        reply = requests.get('http://localhost:3000/tasks/', headers=headers)  # Выводим в консоль оставшиеся записи и закрываем соединение.
    except requests.RequestException:
        print('Communication error')
    else:
        print('Connection=' + reply.headers['Connection'])  # Можно проверять статус подключения.
        if reply.status_code == requests.codes.ok:
            show(reply.json())
        elif reply.status_code == requests.codes.not_found: 
            print('Resourse not found')
        else:
            print('Server error')


def add_task():
    '''Функция, позволяющая создать новую задачу.'''
    h_close = {'Connection': 'Close'}  # Переменная для закрытия потока.
    h_content = {'Content-Type': 'application/json'}
    new_id = int(input('Введите id: '))
    new_name = input('Введите задачу: ')
    new_priority = int(input('Введите приоритет задачи: '))
    new_task = {
        'id': new_id,
        'name': new_name,
        'priority': new_priority,
    }
    print(json.dumps(new_task))
    try:
        reply = requests.post('http://localhost:3000/tasks/', headers=h_content, \
                            data=json.dumps(new_task))  # Добавляем запись методом пост.
        print('reply=' + str(reply.status_code))
        reply = requests.get('http://localhost:3000/tasks/', headers=h_close)  # Выводим в консоль оставшиеся записи и закрываем соединение.
    except requests.RequestException:
        print('Communication error')
    else:
        print('Connection=' + reply.headers['Connection'])  # Можно проверять статус подключения.
        if reply.status_code == requests.codes.ok:
            show(reply.json())
        elif reply.status_code == requests.codes.not_found:  
            print('Resourse not found')
        else:
            print('Server error')


def put_task():
    '''Функция, позволяющая изменить существующую задачу.'''
    h_close = {'Connection': 'Close'}  # Переменная для закрытия потока.
    h_content = {'Content-Type': 'application/json'}
    change_id = int(input('Введите id, задачу которого хотите изменить: '))
    change_name = input('Введите новую задачу: ')
    change_priority = int(input('Введите новый приоритет задачи: '))
    change_task = {
        'id': change_id,
        'name': change_name,
        'priority': change_priority,
    }
    print(json.dumps(change_task))
    try:
        reply = requests.put(f'http://localhost:3000/tasks/{change_id}', 
                             headers=h_content, data=json.dumps(change_task))  # Обновление записи методом пут.
        print('reply=' + str(reply.status_code))
        reply = requests.get('http://localhost:3000/tasks/', headers=h_close)  # Выводим в консоль оставшиеся записи и закрываем соединение.
    except requests.RequestException:
        print('Communication error')
    else:
        print('Connection=' + reply.headers['Connection'])  # Можно проверять статус подключения.
        if reply.status_code == requests.codes.ok:
            show(reply.json())
        elif reply.status_code == requests.codes.not_found:  
            print('Resourse not found')
        else:
            print('Server error')


def info():
    '''Функция, отображающая справочную информацию для пользователя.'''
    print('''
    ******************************************************************
    |                        O HELLO THERE!                           |
    |            Введите 1 чтобы посмотреть все записи.               |
    |         Введите 2 чтобы посмотреть одну запись по индексу.      |
    |  Введите 3 чтобы отсортировать записи по возрастанию приоритета.|
    |    Введите 4 чтобы отсортировать записи по убыванию приоритета. |
    |               Введите 5 чтобы удалить запись.                   |
    |              Введите 6 чтобы добавить запись.                   |
    |               Введите 7 чтобы изменить запись.                  |
    |        Введите 8 чтобы отобразить справочную информацию.        |
    |       Введите 9, чтобы узнать о каждой функции подробнее.       |
    |               Введите 0 чтобы завершить программу.              |
    *******************************************************************
    ''')


def show_cond():
    li_of_funcs = [
        show_head, show_empty, show_task, 
        show, show_all, show_one, sort_tasks_from_small_to_big, 
        sort_tasks_from_big_to_small, delete_task, add_task,
        put_task, info
        ]
    for i in li_of_funcs:
        help(i)


def main():
    info()
    user_input = int(input('Введите номер операции: '))
    while user_input != 0:
        print('Для получения справочной информации введите 8.')
        if user_input == 1:
            try:
                show_all()
            except:
                print('Something goes wrong!')

        elif user_input == 2:
            try:
                show_one()
            except:
                print('Something goes wrong!')

        elif user_input == 3:
            try:
                sort_tasks_from_small_to_big()
            except:
                print('Something goes wrong!')

        elif user_input == 4:
            try:
                sort_tasks_from_big_to_small()
            except:
                print('Something goes wrong!')

        elif user_input == 5:
            try:
                delete_task()
            except:
                print('Something goes wrong!')

        elif user_input == 6:
            try:
                add_task()
            except:
                print('Something goes wrong!')

        elif user_input == 7:
            try:
                put_task()
            except:
                print('Something goes wrong!')

        elif user_input == 8:
            info()
        
        elif user_input == 9:
            show_cond()

        else:
            print('Something goes wrong!')
        
        try:    
            user_input = int(input('Введите номер операции: '))
        except:
            print('Ne ponimau.')
    print('Good bye.')


if __name__ == '__main__':
    main()
