# Программа ToDo_CRUD.

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

Представляет собой клиентскую часть для обращения к серверу.

## Установка.

Для запуска и работы с программой проделайте следующие действия:

##### Шаг 1: скопируйте репозиторий.
```
git clone git@github.com:zhenchel/ToDoListJSON.git
```

##### Шаг 2: установите node.js
 - https://nodejs.org/en/download

##### Шаг 3: установите JSON - сервер.
```
npm install -g json-server
```


## Документация.

```
cd ToDo_CRUD
python -m pydoc .\main.py
```

## Возможности программы.

Хост содержит в себе определенный список задач.
При помощи данной клиентской программы возможно делать такие обращения к хосту как:
- Отображение имеющихся задач.
- Отображение одной задачи по индексу.
- Сортировать задачи по убыванию/возрастанию приоритета.
- Удалять задачи.
- Добавлять задачи.
- Изменять задачи.

| HTTP method | URL |
| ------ | ------ |
| GET | http://localhost:3000/tasks |
| POST | http://localhost:3000/tasks/ |
| PUT | http://localhost:3000/tasks/{change_id} |
| DELETE | http://localhost:3000/tasks/{id_del} |
| SORT | http://localhost:3000/tasks/?_sort=priority |

## Запуск программы.

Перед запуском программы необходимо запустить сервер.

Для этого нужно прописать в командной строке следующее:
```
json-server --watch todolist.json
```

Затем запустите программу ToDo_CRUD.py

>Так же программа содержит в себе справочную информацию.
Для ее отображения введите цифру 8.

## Информация для связи.
Если у Вас возникли какие-либо вопросы, обращайтесь на почту chalyk.evgenij@mail.ru

# Всего хорошего!