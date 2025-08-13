import allure
import requests


URL = 'https://qa-scooter.praktikum-services.ru'
@allure.step("Получение списка заказов")
def order_get_list_of_orders_200(generate_random_string):

    response = requests.post(URL+'/api/v1/orders',
                            json=generate_random_order('BLACK'))
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    response = requests.post(URL+'/api/v1/courier',
                            json={
                                "login": login,
                                "password": password,
                                "firstName": first_name
                                }
                              )
    if response.status_code == 201:
        response = requests.post(URL + '/api/v1/courier/login',
                                 json={
                                     "login": login,
                                     "password": password
                                 }
                                 )
        if response.status_code == 200 and "id" in response.json():
            courierId = response.json().split(': ')
    response = requests.post(URL + '/api/v1/orders',
                             json=generate_random_order('BLACK'))
    if response.status_code == 201:
        track = response.json().split(': ')
        response = requests.put(URL + f'/v1/orders/accept/{track}?courierId={courierId}')
        if response.status_code == 200:
            response = requests.get(URL + f'/v1/orders?courierId={courierId}')
    assert response.status_code == 200