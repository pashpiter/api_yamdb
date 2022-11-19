# API_FINAL_YATUBE
##### Данный проект создан для работы с социальной сетью Yatube, где реализованы следующие функции:
- просмотр всех постов
- создание поста
- комментирование постов
- создание подписок на других пользователей

## Запуск проекта в dev-режиме
Клонировать репозиторий и перейти в него в командной строке:
``` 
git clone git@github.com:IgorKrupko-94/yatube_project.git 
```
``` 
cd api_final_yatube 
```
Установите и активируйте виртуальное окружение c учётом версии Python 3.7 (выбираем python не ниже 3.7):
``` 
py -3.7 -m venv venv 
```
Для пользователей Windows:
``` 
source venv/Scripts/activate 
```
Для пользователей Linux и macOS:
``` 
source venv/bin/activate 
```
Обновляем до последней версии пакетный менеджер pip:
``` 
python -m pip install --upgrade pip 
```
Затем нужно установить все зависимости из файла requirements.txt:
``` 
pip install -r requirements.txt 
```
Выполняем миграции:
``` 
python manage.py migrate 
```
Запускаем проект:
``` 
python manage.py runserver 
```

### Примеры работы с API для всех пользователей
###### Для неавторизованных пользователей работа с API доступна в режиме чтения, что-либо изменить или создать не получится.
GET api/v1/posts/ - получить список всех публикаций.
***При указании параметров limit и offset выдача должна работать с пагинацией.***
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
GET api/v1/posts/{id}/ - получение публикации по id
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
GET api/v1/groups/ - получение списка доступных сообществ
```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```
GET api/v1/groups/{id}/ - получение информации о сообществе по id
```
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```
GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

#### Все остальные примеры запросов доступны в документации

# Author
## Igor Krupko