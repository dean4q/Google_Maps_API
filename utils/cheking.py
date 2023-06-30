import json

from requests import Response
"""методы для проверки ответов наших запросов"""

class Cheking():

    """метод для проверки статус-кода"""
    @staticmethod
    def check_status_code(response: Response,status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f'Успешно, статус-код {status_code}')
        else:
            print(f'Ошибка, статус код {status_code}')


    """метод для проверки обязательных полей в теле ответа"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print('Все поля присутствуют')



    """Метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " верен !!!")

    """Метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_search_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print("Слово " + search_word + " присутствует !!!")
        else:
            print('Слово отсутствует')