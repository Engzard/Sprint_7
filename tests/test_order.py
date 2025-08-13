import allure
import requests


URL = 'https://qa-scooter.praktikum-services.ru'
@allure.step("Создание заказа, выбран чёрный цвет")
def order_BLACK_201(generate_random_string):

    response = requests.post(URL+'/api/v1/orders',
                            json=generate_random_order('BLACK'))
    assert response.status_code == 201 and 'track' in response.json()
@allure.step("Создание заказа, выбран серый цвет")
def order_GREY_201(generate_random_string):

    response = requests.post(URL+'/api/v1/orders',
                            json=generate_random_order('GREY'))
    assert response.status_code == 201 and 'track' in response.json()
@allure.step("Создание заказа, не выбран цвет")
def order_not_color_201(generate_random_string):

    response = requests.post(URL+'/api/v1/orders',
                            json=generate_random_order())
    assert response.status_code == 201 and 'track' in response.json()