import json

from requests import Response
from utils.cheking import Cheking
from utils.API import GoogleMapsAPI

"""создание изменение и удаление новой локации"""

class TestCreatePlace():
    def test_create_new_place(self):

        print('Метод POST')
        result_post: Response = GoogleMapsAPI.create_new_location()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        print(result_post.status_code)
        token = json.loads(result_post.text)
        Cheking.check_json_value(result_post, 'status', 'OK')

        print("метод GET POST")
        result_get = GoogleMapsAPI.get_new_location(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_token(result_get,['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        token = json.loads(result_get.text)
        print(list(token))
        Cheking.check_json_value(result_get, 'address', '29, side layout, cohen 09')
        # "address": "29, side layout, cohen 09",

        print("метод PUT")
        result_put = GoogleMapsAPI.put_new_location(place_id)
        Cheking.check_status_code(result_put, 200)
        Cheking.check_json_token(result_put, ['msg'])
        Cheking.check_json_value(result_put,'msg', 'Address successfully updated' )

        print("метод GET PUT")
        result_get = GoogleMapsAPI.get_new_location(place_id)
        Cheking.check_status_code(result_get, 200)

        print("метод DELETE")
        result_delete = GoogleMapsAPI.delete_new_location(place_id)
        Cheking.check_status_code(result_delete, 200)
        Cheking.check_json_token(result_delete,['status'])
        token = json.loads(result_delete.text)

        print(list(token))


        print("метод GET DELETE")
        result_get = GoogleMapsAPI.get_new_location(place_id)
        Cheking.check_status_code(result_get, 404)
        Cheking.check_json_token(result_get, ['msg'])
        token = json.loads(result_post.text)
        # Cheking.check_json_value(result_delete, 'msg', "Delete operation failed, looks like the data doesn't exists")
        Cheking.check_json_search_in_value(result_get, 'msg', 'like')

        print()
        print('Тестирование создания ,изменения и удаления новой локации выполнено')