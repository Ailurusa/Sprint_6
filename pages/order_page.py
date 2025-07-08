import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Кликнуть на кнопку Заказать")
    def click_order_button(self, order_button):
        self.scroll_to_element(order_button)
        self.click_on_element(order_button)

    @allure.step("Заполнить первую страницу заказа")
    def fill_first_order_form(self, name, surname, address, telephone):
        self.add_text_to_element(OrderPageLocators.INPUT_FIRST_NAME, name)
        self.add_text_to_element(OrderPageLocators.INPUT_LAST_NAME, surname)
        self.add_text_to_element(OrderPageLocators.INPUT_DELIVERY_ADDRESS, address)
        self.add_text_to_element(OrderPageLocators.INPUT_PHONE_NUMBER, telephone)

    @allure.step("Выбрать станцию метро")
    def choose_metro(self, station_name):
        self.click_on_element(OrderPageLocators.INPUT_METRO_STATION)
        self.add_text_to_element(OrderPageLocators.INPUT_METRO_STATION, station_name)
        dynamic_locator = (
            OrderPageLocators.METRO_OPTION_BY_NAME[0], OrderPageLocators.METRO_OPTION_BY_NAME[1].format(station_name))
        self.click_on_element(dynamic_locator)

    @allure.step("Нажать кнопку Далее")
    def click_button_further(self):
        self.click_on_element(OrderPageLocators.BTN_CONTINUE_TO_RENT)

    @allure.step("Заполнить вторую страницу заказа")
    def fill_second_order_form(self, date, comment):
        self.add_text_to_element(OrderPageLocators.INPUT_DATE, date)
        self.add_text_to_element(OrderPageLocators.INPUT_COMMENT, comment)

    @allure.step("Выбрать срок аренды самоката")
    def choose_rental_period(self):
        self.click_on_element(OrderPageLocators.DROPDOWN_RENT_DURATION)
        self.click_on_element(OrderPageLocators.RENT_OPTION_ONE_DAY)

    @allure.step("Выбрать цвет самоката")
    def choose_scooter_color(self):
        self.click_on_element(OrderPageLocators.CHECKBOX_COLOR_BLACK)

    @allure.step("Кликнуть на кнопку Заказать")
    def click_button_order(self):
        self.click_on_element(OrderPageLocators.BTN_SUBMIT_ORDER)

    @allure.step("Подтвердить заказ")
    def click_button_yes(self):
        self.click_on_element(OrderPageLocators.BTN_CONFIRM_YES)

    @allure.step('Оформить заказ самоката')
    def order_scooter(self, order_button, order_data):
        self.click_order_button(order_button)
        self.fill_first_order_form(
            order_data['first_name'],
            order_data['last_name'],
            order_data['address'],
            order_data['phone_number']
        )
        self.choose_metro(order_data['subway_station'])
        self.click_button_further()
        self.choose_rental_period()
        self.choose_scooter_color()
        self.fill_second_order_form(
            order_data['date'],
            order_data['comment']
        )
        self.click_button_order()
        self.click_button_yes()
        return self.get_text(OrderPageLocators.MODAL_CONFIRM_TITLE)
