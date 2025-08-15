import allure


class TestAccount:
    @allure.title("Авторизация курьера в системе")
    def test_career_log_in_200(self, generate_random_string, create_courier, login_courier):
        login = generate_random_string(10)
        password = generate_random_string(10)
        with allure.step(f"Отправка POST-запроса на создание курьера"):
            response = create_courier(login, password)
        with allure.step(f"Отправка POST-запроса на авторизацию курьера"):
            response = login_courier(login, password)
        with allure.step("Проверка кода ответа и тела JSON"):
            assert response.status_code == 200 and "id" in response.json()
    @allure.title("Авторизация курьера в системе без логина")
    def test_career_log_in_without_login_400(self, generate_random_string, create_courier, login_courier):
        login = generate_random_string(10)
        password = generate_random_string(10)
        with allure.step(f"Отправка POST-запроса на создание курьера"):
            response = create_courier(login, password)
        with allure.step(f"Отправка POST-запроса на авторизацию курьера"):
            response = login_courier(None, password)
        with allure.step("Проверка кода ответа и тела JSON"):
            assert (response.status_code == 400) and "Недостаточно данных для входа" in response.json
    @allure.title("Авторизация курьера в системе без пароля")
    def test_career_log_in_without_password_400(self, generate_random_string, create_courier, login_courier):
        login = generate_random_string(10)
        password = generate_random_string(10)
        with allure.step(f"Отправка POST-запроса на создание курьера"):
            response = create_courier(login, password)
        with allure.step(f"Отправка POST-запроса на авторизацию курьера"):
            response = login_courier(login)
        with allure.step("Проверка кода ответа и тела JSON"):
            assert (response.status_code == 400) and "Недостаточно данных для входа" in response.json
    @allure.title("Авторизация курьера в системе с неверным паролем")
    def test_career_log_in_wrong_password_404(self, generate_random_string, create_courier, login_courier):
        login = generate_random_string(10)
        password = generate_random_string(10)
        with allure.step(f"Отправка POST-запроса на создание курьера"):
            response = create_courier(login, password)
        with allure.step(f"Отправка POST-запроса на авторизацию курьера"):
            response = login_courier(login, password+'1')
        with allure.step("Проверка кода ответа и тела JSON"):
            assert response.status_code == 404 and response.json().get("message") == "Учетная запись не найдена"
    @allure.title("Авторизация курьера в системе с неверным логином")
    def test_career_log_in_wrong_login_404(self, generate_random_string, create_courier, login_courier):
        login = generate_random_string(10)
        password = generate_random_string(10)
        with allure.step(f"Отправка POST-запроса на создание курьера"):
            response = create_courier(login, password)
        with allure.step(f"Отправка POST-запроса на авторизацию курьера"):
            response = login_courier(login+'1', password)
        with allure.step("Проверка кода ответа и тела JSON"):
            assert response.status_code == 404 and response.json().get("message") == "Учетная запись не найдена"