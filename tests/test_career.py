import allure
import requests

URL = 'https://qa-scooter.praktikum-services.ru'
@allure.step("создание курьера")
def career_creation(generate_random_string):


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
    assert response.status_code == 201 and response.json() == {"ok": True}
@allure.step("Создание двух курьеров с одним логином")
def duble_career_creation_return_409(generate_random_string):
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    response = requests.post(URL + '/api/v1/courier',
                             json={
                                 "login": login,
                                 "password": password,
                                 "firstName": first_name
                             }
                             )
    duble_response = requests.post(URL + '/api/v1/courier',
                             json={
                                 "login": login,
                                 "password": password,
                                 "firstName": first_name
                             }
                             )
    assert duble_response.status_code == 409
@allure.step("Создание курьера без логина")
def career_creation_without_login_400(generate_random_string):
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    response = requests.post(URL + '/api/v1/courier',
                             json={
                                 "password": password,
                                 "firstName": first_name
                             }
                             )
    assert response.status_code == 400
@allure.step("Создание курьера без пароля")
def career_creation_without_password_return_400(generate_random_string):
    login = generate_random_string(10)
    first_name = generate_random_string(10)
    response = requests.post(URL + '/api/v1/courier',
                             json={
                                 "login": login,
                                 "firstName": first_name
                             }
                             )
    assert response.status_code == 400

