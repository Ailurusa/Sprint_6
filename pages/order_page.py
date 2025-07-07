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
        self.add_text_to_element(OrderPageLocators.input_first_name, name)
        self.add_text_to_element(OrderPageLocators.input_last_name, surname)
        self.add_text_to_element(OrderPageLocators.input_delivery_address, address)
        self.add_text_to_element(OrderPageLocators.input_phone_number, telephone)

    @allure.step("Выбрать станцию метро")
    def choose_metro(self, station_name):
        self.click_on_element(OrderPageLocators.input_metro_station)
        self.add_text_to_element(OrderPageLocators.input_metro_station, station_name)
        dynamic_locator = (
            OrderPageLocators.metro_option_by_name[0], OrderPageLocators.metro_option_by_name[1].format(station_name))
        self.click_on_element(dynamic_locator)

    @allure.step("Нажать кнопку Далее")
    def click_button_further(self):
        self.click_on_element(OrderPageLocators.btn_continue_to_rent)

    @allure.step("Заполнить вторую страницу заказа")
    def fill_second_order_form(self, date, comment):
        self.add_text_to_element(OrderPageLocators.input_date, date)
        self.add_text_to_element(OrderPageLocators.input_comment, comment)

    @allure.step("Выбрать срок аренды самоката")
    def choose_rental_period(self):
        self.click_on_element(OrderPageLocators.dropdown_rent_duration)
        self.click_on_element(OrderPageLocators.rent_option_one_day)

    @allure.step("Выбрать цвет самоката")
    def choose_scooter_color(self):
        self.click_on_element(OrderPageLocators.checkbox_color_black)

    @allure.step("Кликнуть на кнопку Заказать")
    def click_button_order(self):
        self.click_on_element(OrderPageLocators.btn_submit_order)

    @allure.step("Подтвердить заказ")
    def click_button_yes(self):
        self.click_on_element(OrderPageLocators.btn_confirm_yes)

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
        return self.get_text(OrderPageLocators.modal_confirm_title)
