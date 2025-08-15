import pytest
import requests

URL = 'https://qa-scooter.praktikum-services.ru'

@pytest.fixture
def register_new_courier_and_return_login_password(generate_random_string):
    login = generate_random_string
    password = generate_random_string
    first_name = generate_random_string

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(URL+'/api/v1/courier', data=payload)


    return payload

@pytest.fixture
def create_courier(login = None , password = None, first_name = None):
    payload = {}
    payload['login'] = login
    payload['password'] = password
    payload['firstName'] = first_name
    return requests.post(URL+'/api/v1/courier',json=payload)
@pytest.fixture
def login_courier(login = None , password = None):
    payload = {}
    payload['login'] = login
    payload['password'] = password
    return requests.post(URL+'/api/v1/courier/login',json=payload)

@pytest.fixture
def generate_random_order(generate_payload_order,color = None):
    return requests.post(URL + '/api/v1/orders',
                             json=generate_payload_order(color))
@pytest.fixture
def accept_order(track, courierId):
    return requests.put(URL + f'/v1/orders/accept/{track}?courierId={courierId}')
@pytest.fixture
def list_order(courierId):
    return requests.get(URL + f'/v1/orders?courierId={courierId}')
