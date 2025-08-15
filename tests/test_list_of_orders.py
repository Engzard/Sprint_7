import allure

class TestOrderList:
    @allure.title("Получение списка заказов")
    def test_order_get_list_of_orders_200(self, generate_random_string, create_courier, login_courier,
                                          generate_random_order, accept_order, list_order):
        login = generate_random_string(10)
        password = generate_random_string(10)
        with allure.step(f"Отправка POST-запроса на создание курьера"):
            response = create_courier(login, password)
        with allure.step(f"Отправка POST-запроса на авторизацию курьера"):
            response = login_courier(login, password)
        with allure.step(f"Получение id курьера"):
            courierId = response.json().split(': ')
        with allure.step(f"Создание заказа"):
            response = generate_random_order('BLACK')
        with allure.step(f"Получение номера заказа"):
            track = response.json().split(': ')
        with allure.step(f"Принятие заказа"):
            response = accept_order(track, courierId)
        with allure.step(f"Получение списка заказов"):
            response = list_order(courierId)
        with allure.step("Проверка кода ответа"):
            assert response.status_code == 200