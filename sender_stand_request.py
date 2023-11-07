import configuration
import requests
import data


def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count": 20})


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers
                         )


def post_products_kits(ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=ids,
                         headers=data.headers
                         )


print(get_users_table().text)
#responce = post_products_kits(data.product_ids)
#print(responce.status_code)
#print(responce.json())
#print(responce.json())


#response = post_new_user(data.user_body1)
#print(response.json())

#responce = get_users_table()
#print(response.status_code)
#print(response.text)