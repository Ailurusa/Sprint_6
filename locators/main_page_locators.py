from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.ID, 'accordion__heading-{}'
    ANSWER_LOCATOR = By.XPATH, './/div[@id = "accordion__panel-{}"]/p'

    BTN_TOP_ORDER = By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"
    BTN_MAIN_ORDER = By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"
