

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
