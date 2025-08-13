import allure
import requests


URL = 'https://qa-scooter.praktikum-services.ru'
@allure.step("Авторизация курьера в системе")
def career_log_in_200(generate_random_string):
    login = generate_random_string(10)
    password = generate_random_string(10)
    response = requests.post(URL + '/api/v1/courier',
                             json={
                                 "login": login,
                                 "password": password
                             }
                             )
    if response.status_code == 201:
        response = requests.post(URL + '/api/v1/courier/login',
                                 json={
                                     "login": login,
                                     "password": password
                                 }
                                 )
    assert response.status_code == 200 and "id" in response.json()
@allure.step("Авторизация курьера в системе без логина")
def career_log_in_without_login_400(generate_random_string):
    login = generate_random_string(10)
    password = generate_random_string(10)
    response = requests.post(URL + '/api/v1/courier',
                             json={
                                 "login": login,
                                 "password": password
                             }
                             )
    if response.status_code == 201:
        response = requests.post(URL + '/api/v1/courier/login',
                                 json={
                                     "password": password
                                 }
                                 )
    assert response.status_code == 400
@allure.step("Авторизация курьера в системе без пароля")
def career_log_in_without_password_400(generate_random_string):
    login = generate_random_string(10)
    password = generate_random_string(10)
    response = requests.post(URL + '/api/v1/courier',
                             json={
                                 "login": login,
                                 "password": password
                             }
                             )
    if response.status_code == 201:
        response = requests.post(URL + '/api/v1/courier/login',
                                 json={
                                     "login": login
                                 }
                                 )
    assert response.status_code == 400
@allure.step("Авторизация курьера в системе с неверным паролем")
def career_log_in_wrong_password_404(generate_random_string):
    login = generate_random_string(10)
    password = generate_random_string(10)
    response = requests.post(URL + '/api/v1/courier',
                             json={
                                 "login": login,
                                 "password": password
                             }
                             )
    if response.status_code == 201:
        response = requests.post(URL + '/api/v1/courier/login',
                                 json={
                                     "login": login,
                                     "password": password+'1'
                                 }
                                 )
    assert response.status_code == 404 and response.json().get("message") == "Учетная запись не найдена"
@allure.step("Авторизация курьера в системе с неверным логином")
def career_log_in_wrong_login_404(generate_random_string):
    login = generate_random_string(10)
    password = generate_random_string(10)
    response = requests.post(URL + '/api/v1/courier',
                             json={
                                 "login": login,
                                 "password": password
                             }
                             )
    if response.status_code == 201:
        response = requests.post(URL + '/api/v1/courier/login',
                                 json={
                                     "login": login+'1',
                                     "password": password
                                 }
                                 )
    assert response.status_code == 404 and response.json().get("message") == "Учетная запись не найдена"