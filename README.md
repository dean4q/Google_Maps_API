

# Google_Maps_API
Построение базового проекта по автоматизации тестирования на Pytest.
Данный проект был написан для демонстрации бызовых возможностей Pytest
на основе одного из курсов на Stepik.


Сначала создадим новый проект в PyCharm (например Google_Maps).
Далее нужно создать директорию в этом проекте utils,
в этой директории создать новый файл http_methods, где будет создан класс HttpMethods 
для работы с запросами GET, POST, PUT и DELETE
```
import requests
"""Список http - методов"""
class HttpMethods():
    headers = {'Content-Type': 'application/json'}
    cookie= ''


    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return  result

    @staticmethod
    def post(url,body):
        result = requests.post(url,json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def put(url,body):
        result = requests.put(url,json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result
```

Далее создаем новый файл API.py куда будут занесены методы для работы с API.
импортируем http-методы,которые написали ранее
```
from utils.http_methods import HttpMethods
```
так-же нам нужны базовая url и параметр запросок,которые берем из документации.
```
base_url = "https://rahulshettyacademy.com"  # базовая url
key = "?key=qaclick123"  # параметр для всех запросов
```
Создаем класс GoogleMapsAPI,где будут написаны методы для создания,изменения,получения информации и удаления локации(POST, PUT, GET и DELETE)
Добавим метод для создания новой локации и обернем его в декоратор ```@staticmethod```

```
def create_new_location():                           
        json_for_create_new_place = {                           #создаем json- переменную,берем из документации
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resourse = '/maps/api/place/add/json'                                # ресурс метода POST,берется из документации
        post_url = base_url + post_resourse + key                                 #собираем ссылку для запроса путем конкатенации
        print(post_url)                                                           #выводим на печать ссылку для проверки на корректность           
        result_post = HttpMethods.post(post_url, json_for_create_new_place)       #получаем результат запроса,обращаясь к методу HttpMethods.post
        print(result_post.text)         #выводим результат в текстовом виде
        return result_post
```
после создания новой локации,в ответе на запрос будет получен ответ в формате json,например
```
{
    "status": "OK",
    "place_id": "d50056f5ca96b8854fe132dd311729e2",
    "scope": "APP",
    "reference": "948dedaf1a0f2dec95fa8807084f1acb948dedaf1a0f2dec95fa8807084f1acb",
    "id": "948dedaf1a0f2dec95fa8807084f1acb"
}
```
Теперь добавим метод для проверки новой локации
```
 @staticmethod
    def get_new_location(place_id):
        get_resourse = '/maps/api/place/get/json'                                 # ресурс метода GET,берется из документации 
        get_url = base_url + get_resourse + key + '&place_id=' + place_id         #place_id мы берем из ответа на создание новой локации
        print(get_url)                                                            #выводим на печать ссылку для проверки на корректность
        result_get = HttpMethods.get(get_url)                                     #получаем результат запроса,обращаясь к методу HttpMethods.get
        print(result_get.text)
        return result_get
```

Создадим метод для обновления локации
```
    @staticmethod
    def put_new_location(place_id):
        put_resourse = '/maps/api/place/update/json'                              # ресурс метода PUT, берется из документации
        put_url = base_url + put_resourse + key                              
        json_for_update_new_location = {                                          # создаем новый json для изменения локации
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        print(put_url)                                                            #выводим на печать ссылку для проверки на корректность
        result_put = HttpMethods.put(put_url, json_for_update_new_location)       #получаем результат запроса,обращаясь к методу HttpMethods.put
        print(result_put.text)
        return result_put
```
И остается последний метод для удаления локации
```
@staticmethod
    def delete_new_location(place_id):
        delete_resourse = '/maps/api/place/delete/json'                          # ресурс метода DELETE, берется из документации
        delete_url = base_url + delete_resourse + key
        json_for_delete_new_location = {                                         #создаем json с указанием существующего place_id
            "place_id": place_id
        }
        print(delete_url)
        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_location)   #получаем результат запроса,обращаясь к методу HttpMethods.delete
        print(result_delete.text)
        return result_delete
```
Создаем  файл cheking.py, где будут храниться методы для проверки ответов наших запросов,импортируем необходимые библиотеки и создаем класс
```
import json
from requests import Response
class Cheking():
```
теперь добавляем все проверки.
Проверка на статус-код
```
@staticmethod
    def check_status_code(response: Response,status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f'Успешно, статус-код {status_code}')
        else:
            print(f'Ошибка, статус код {status_code}')
```

метод для проверки обязательных полей в теле ответа
```
@staticmethod
def check_json_token(response: Response, expected_value):
    token = json.loads(response.text)
    assert list(token) == expected_value
    print('Все поля присутствуют')
```

Метод для проверки значений обязательных полей в ответе запроса
```
@staticmethod
def check_json_value(result, field_name, expected_value):
    check = result.json()
    check_info = check.get(field_name)
    assert check_info == expected_value
    print(field_name + " верен !!!")
```

Метод для проверки значений обязательных полей в ответе запроса
```
@staticmethod
def check_json_search_in_value(result, field_name, search_word):
    check = result.json()
    check_info = check.get(field_name)
    if search_word in check_info:
        print("Слово " + search_word + " присутствует !!!")
    else:
        print('Слово отсутствует')
```

Создадим в корневой директории проекта папку tests и создадим в этой папке файл test_Google_maps_API.py.
слово test в названии файла является обязательным,это нужно для того,чтобы Pytest смог увидеть его именно как файл с тестами.
Импортируем нужные библиотеки для работы
```
import json
from requests import Response
from utils.cheking import Cheking
from utils.API import GoogleMapsAPI
```
И создадим класс ```TestCreatePlace```,в котором будут шаги тестирования.
Приступим к написанию метода
```
def test_create_new_place(self):
```

в него будем добавлять все действия 
метод POST
```
print('Метод POST')                                                           # выведем название,для визуального разделения методов 
result_post: Response = GoogleMapsAPI.create_new_location()                   # обращаемся к методу через импортированный класс
check_post = result_post.json()                                               # получаем ответ в формате json
place_id = check_post.get("place_id")                                         # с полученного ответа сохраняем place_id в отдельную переменную
Cheking.check_status_code(result_post, 200)                                   # проверка статус-кода
Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])    # проверяем обязательные поля в ответе
print(result_post.status_code)
token = json.loads(result_post.text)
Cheking.check_json_value(result_post, 'status', 'OK')                         # проверка на значение полей согласно документации
```

метод GET (получаем информацию о созданной локации)
```
print("метод GET POST")
result_get = GoogleMapsAPI.get_new_location(place_id)
Cheking.check_status_code(result_get, 200)
Cheking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
token = json.loads(result_get.text)
print(list(token))
Cheking.check_json_value(result_get, 'address', '29, side layout, cohen 09')
```

метод PUT
```
print("метод PUT")
result_put = GoogleMapsAPI.put_new_location(place_id)
Cheking.check_status_code(result_put, 200)
Cheking.check_json_token(result_put, ['msg'])
Cheking.check_json_value(result_put,'msg', 'Address successfully updated' )
```
метод GET  (получаем информацию об обновленной локации)
```
print("метод GET PUT")
result_get = GoogleMapsAPI.get_new_location(place_id)
Cheking.check_status_code(result_get, 200)
```

метод DELETE
```
print("метод DELETE")
result_delete = GoogleMapsAPI.delete_new_location(place_id)
Cheking.check_status_code(result_delete, 200)
Cheking.check_json_token(result_delete,['status'])
token = json.loads(result_delete.text)
```

метод GET  (получаем информацию об удаленной локации)
```
print("метод GET DELETE")
result_get = GoogleMapsAPI.get_new_location(place_id)
Cheking.check_status_code(result_get, 404)
Cheking.check_json_token(result_get, ['msg'])
token = json.loads(result_post.text)
Cheking.check_json_search_in_value(result_get, 'msg', 'like')
```

после написания кода нужно отклыть терминал в PyCharm и перейьти в директорию с проектом,для этого ввести в терминале команду
```
cd <путь к директории>
```
после чего ввести 
```
python3 -m pytest -s -v
```
