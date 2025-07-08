import allure

from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Кликнуть на вопрос из блока FAQ')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_element(locator_q_formatted)
        self.wait.until(EC.element_to_be_clickable(locator_q_formatted))
        self.click_on_element(locator_q_formatted)

    @allure.step('Получить текст ответа на вопрос')
    def get_answer_text(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text(locator_a_formatted)

    @allure.step('Проверить текст ответа')
    def check_question_and_answer(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)
