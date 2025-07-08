from selenium.webdriver.common.by import By


class OrderPageLocators:
    INPUT_FIRST_NAME = (By.CSS_SELECTOR, '[placeholder="* Имя"]')
    INPUT_LAST_NAME = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')
    INPUT_DELIVERY_ADDRESS = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')
    INPUT_METRO_STATION = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    INPUT_PHONE_NUMBER = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')
    BTN_CONTINUE_TO_RENT = (By.XPATH, '//button[text()="Далее"]')
    METRO_OPTION_BY_NAME = (By.XPATH, '//div[text()="{}"]')
    INPUT_DATE = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')
    DROPDOWN_RENT_DURATION = (By.CLASS_NAME, 'Dropdown-placeholder')
    RENT_OPTION_ONE_DAY = (By.XPATH, '//div[text()="сутки"]')
    CHECKBOX_COLOR_BLACK = (By.ID, 'black')
    CHECKBOX_COLOR_GRAY = (By.ID, 'grey')
    INPUT_COMMENT = (By.CSS_SELECTOR, '[placeholder="Комментарий для курьера"]')
    BTN_SUBMIT_ORDER = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]')
    MODAL_CONFIRM_TITLE = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    BTN_CONFIRM_YES = (By.XPATH, '//button[text()="Да"]')
