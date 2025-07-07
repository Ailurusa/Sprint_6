import allure
import pytest

import data
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Проверка успешного оформления заказа')
    @allure.description('Заполняем форму заказа с разными наборами данных и проверяем, что заказ успешно оформлен.')
    @pytest.mark.parametrize('locator, order_data', [
        (MainPageLocators.btn_top_order, data.order_data_1),
        (MainPageLocators.btn_main_order, data.order_data_2)
    ])
    def test_create_order(self, driver, locator, order_data):
        order_page = OrderPage(driver)
        assert 'Заказ оформлен' in order_page.order_scooter(locator, order_data)
