from selenium.webdriver.common.by import By


class MainPageLocators:
    question_locator = By.ID, 'accordion__heading-{}'
    answer_locator = By.XPATH, './/div[@id = "accordion__panel-{}"]/p'

    btn_top_order = By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"
    btn_main_order = By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"
