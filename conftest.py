import pytest
import requests
import string
import random


@pytest.fixture
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string
@pytest.fixture
def generate_random_address(generate_random_string):
    simbol = {',', '.', '-'}
    addr = (generate_random_string(random.randint(3,9)) + ',' + generate_random_string(random.randint(2,4)) + simbol[random.randint(0,2)] + generate_random_string(random.randint(3,9)))
    return addr
@pytest.fixture
def generate_random_phone():
    return f"+7 {"".join([str(random.randint(0, 9)) for _ in range(3)])} {"".join([str(random.randint(0, 9)) for _ in range(3)])} {"".join([str(random.randint(0, 9)) for _ in range(2)])} {"".join([str(random.randint(0, 9)) for _ in range(2)])}"

@pytest.fixture
def generate_random_date():
    return f"2025-{''.join([str(random.randint(9, 12))])}-{''.join([str(random.randint(1, 31))])}"

@pytest.fixture
def generate_random_order(color = None):

    last_name = generate_random_string(10)
    address = generate_random_address()
    first_name = generate_random_string(10)
    phone = generate_random_phone()
    date = generate_random_date()
    payload={
                "firstName": first_name,
                "lastName": last_name,
                "address": address,
                "metroStation": 4,
                "phone": phone,
                "rentTime": 5,
                "deliveryDate": date,
                "comment": f"{generate_random_string(random.randint(4, 11))}, {generate_random_string(random.randint(4, 7))}. {generate_random_string(random.randint(3, 9))}!",
                "color": color
            }
    return payload

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

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    #if response.status_code == 201:

    return payload