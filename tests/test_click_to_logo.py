import allure
import pytest

import urls
from locators.general_locators import GeneralLocators
from locators.logo_locators import LogoLocators
from pages.check_logo import CheckLogo


class TestClickToLogo:
    @allure.title('Проверка перехода на главную страницу Самоката по клику на логотип')
    @allure.description(
        'Переход осуществляется со страницы оформления заказа. Проверяем, что открывается главная страница.')
    def test_go_to_scooter_home_page_by_clicking_on_scooter_logo(self, driver):
        logo_page = CheckLogo(driver)
        logo_page.open_order_page()
        logo_page.transition_via_logo(LogoLocators.LOGO_SCOOTER)
        assert logo_page.is_transition_successful(urls.BASE_URL, GeneralLocators.IMG_MAIN_PAGE_SCOOTER)

    @allure.title('Проверка перехода на Dzen по клику на логотип Яндекса')
    @allure.description(
        'Переход осуществляется со страницы оформления заказа. Проверяем, что открывается страница Dzen.')
    def test_go_to_dzen_by_clicking_on_yandex_logo(self, driver):
        logo_page = CheckLogo(driver)
        logo_page.open_order_page()
        logo_page.transition_via_logo(LogoLocators.LOGO_YANDEX)
        assert logo_page.is_transition_successful(urls.DZEN_URL, GeneralLocators.BUTTON_DZEN_SEARCH)
