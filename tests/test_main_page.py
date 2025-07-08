import allure
import pytest

from data import answers
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка раскрытия вопросов FAQ')
    @allure.description('Кликаем по каждому вопросу блока FAQ и проверяем, что отображается корректный ответ.')
    @pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_faq_question_displays_correct_answer(self, driver, num):
        main_page = MainPage(driver)
        assert main_page.check_question_and_answer(num) == answers[num]
