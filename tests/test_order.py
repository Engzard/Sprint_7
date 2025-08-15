import allure

class TestOrder:

    @allure.title("Создание заказа, выбран чёрный цвет")
    def test_order_BLACK_201(self, generate_random_order):
        with allure.step(f"Создание заказа"):
            response = generate_random_order('BLACK')
        with allure.step("Проверка кода ответа и тела JSON"):
            assert response.status_code == 201 and 'track' in response.json()
    @allure.title("Создание заказа, выбран серый цвет")
    def test_order_GREY_201(self, generate_random_order):
        with allure.step(f"Создание заказа"):
            response = generate_random_order('GREY')
        with allure.step("Проверка кода ответа и тела JSON"):
            assert response.status_code == 201 and 'track' in response.json()
    @allure.title("Создание заказа, не выбран цвет")
    def test_order_not_color_201(self, generate_random_order):
        with allure.step(f"Создание заказа"):
            response = generate_random_order()
        with allure.step("Проверка кода ответа и тела JSON"):
            assert response.status_code == 201 and 'track' in response.json()