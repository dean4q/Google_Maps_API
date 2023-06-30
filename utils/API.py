from utils.http_methods import HttpMethods
from utils.cheking import Cheking
"""методы для тестирования google maps API """
base_url = "https://rahulshettyacademy.com"  # базовая url
key = "?key=qaclick123"  # параметр для всех запросов


class GoogleMapsAPI():
    """метод для создания новой локации"""

    @staticmethod
    def create_new_location():
        json_for_create_new_place = {
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

        post_resourse = '/maps/api/place/add/json'  # ресурс метода POST
        post_url = base_url + post_resourse + key
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """метод для проверки новой локации"""

    @staticmethod
    def get_new_location(place_id):
        get_resourse = '/maps/api/place/get/json'  # ресурс метода GET
        get_url = base_url + get_resourse + key + '&place_id=' + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    """метод для изменения новой локации"""

    @staticmethod
    def put_new_location(place_id):
        put_resourse = '/maps/api/place/update/json'  # ресурс метода PUT
        put_url = base_url + put_resourse + key
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        print(put_url)
        result_put = HttpMethods.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put

    """метод для удаления новой локации"""
    @staticmethod
    def delete_new_location(place_id):
        delete_resourse = '/maps/api/place/delete/json'  # ресурс метода DELETE
        delete_url = base_url + delete_resourse + key
        json_for_delete_new_location = {
            "place_id": place_id
        }
        print(delete_url)
        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete
