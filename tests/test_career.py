import allure
from helpers import create_courier
class TestOrder:
    @allure.title("создание курьера")
    def test_career_creation(self, generate_random_string, create_courier):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        with allure.step (f"Отправка POST-запроса на создание курьера"):
            response = create_courier(login, password, first_name)
        with allure.step("Проверка кода ответа и тела JSON"):
            assert response.status_code == 201 and response.json() == {"ok": True}
    @allure.title("Создание двух курьеров с одним логином")
    def test_duble_career_creation_return_409(self, generate_random_string, create_courier):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        with allure.step (f"Отправка POST-запроса на создание первого курьера"):
            response = create_courier(login, password, first_name)

        with allure.step (f"Отправка POST-запроса на создание второго курьера"):
            duble_response = create_courier(login, password, first_name)
        with allure.step("Проверка кода ответа и тела JSON"):
            assert duble_response.status_code == 409 and '"message": "Этот логин уже используется"' in duble_response.json()
    @allure.title("Создание курьера без логина")
    def test_career_creation_without_login_400(self, generate_random_string, create_courier):
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        with allure.step (f"Отправка POST-запроса на создание курьера"):
            response = create_courier(None,password, first_name)
        with allure.step("Проверка кода ответа и тела JSON"):
            assert (response.status_code == 400) and "Недостаточно данных для создания учетной записи" in response.json

    @allure.title('Создание курьера без пароля')
    def test_career_creation_without_password_return_400(self, generate_random_string, create_courier):
        login = generate_random_string(10)
        first_name = generate_random_string(10)
        with allure.step (f"Отправка POST-запроса на создание курьера"):
            response = create_courier(login, None, first_name)
        with allure.step("Проверка кода ответа и тела JSON"):
            assert (response.status_code == 400) and "Недостаточно данных для создания учетной записи" in response.json
