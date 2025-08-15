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
def generate_random_order(generate_payload_order,color = None):
    return requests.post(URL + '/api/v1/orders',
                             json=generate_payload_order(color))
@pytest.fixture
def accept_order(track, courierId):
    return requests.put(URL + f'/v1/orders/accept/{track}?courierId={courierId}')
@pytest.fixture
def list_order(courierId):
    return requests.get(URL + f'/v1/orders?courierId={courierId}')

