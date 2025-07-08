import allure

import urls
from locators.general_locators import GeneralLocators
from locators.logo_locators import LogoLocators
from pages.base_page import BasePage


class CheckLogo(BasePage):
    @allure.step("Перейти на страницу заказа")
    def open_order_page(self):
        self.driver.get(urls.ORDER_URL)

    @allure.step('Кликнуть по логотипу и переключиться на новую вкладку')
    def transition_via_logo(self, logo_locator):
        self.click_on_element(logo_locator)
        self.switch_to_last_tab()

    @allure.step('Проверить успешный переход на нужный URL и наличие элемента')
    def is_transition_successful(self, expected_url, element_locator):
        self.wait_for_url(expected_url)
        return self.find_element_with_wait(element_locator).is_displayed()

    @allure.step('Кликнуть по логотипу Яндекса и проверить переход')
    def check_yandex_logo_transition(self):
        self.transition_via_logo(LogoLocators.LOGO_YANDEX)
        return self.is_transition_successful(urls.DZEN_URL, GeneralLocators.BUTTON_DZEN_SEARCH)

    @allure.step('Кликнуть по логотипу Самоката и проверить переход')
    def check_scooter_logo_transition(self):
        self.transition_via_logo(LogoLocators.LOGO_SCOOTER)
        return self.is_transition_successful(urls.BASE_URL, GeneralLocators.IMG_MAIN_PAGE_SCOOTER)
