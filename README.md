

# Google_Maps_API
Построение базового проекта по автоматизации тестирования на Pytest.
Данный проэкт был написан для демонстрации бызовых возможностей Pytest
на основе одного из курсов на Stepik.


Сначала создадим новый проэкт в PyCharm (например Google_Maps).
Далее нужно создать директорию в этом проэкте utils,
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

        post_resourse = '/maps/api/place/add/json'  # ресурс метода POST,берется из документации
        post_url = base_url + post_resourse + key   #собираем ссылку для запроса путем конкатенации
        print(post_url)                             #выводим на печать ссылку для проверки на корректность           
        result_post = HttpMethods.post(post_url, json_for_create_new_place)       #получаем результат запроса,обращаясь к методу HttpMethods.post
        print(result_post.text)         #выводим результат в текстовом виде
        return result_post
```
