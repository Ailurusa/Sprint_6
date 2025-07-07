from selenium.webdriver.common.by import By


class OrderPageLocators:
    input_first_name = (By.CSS_SELECTOR, '[placeholder="* Имя"]')
    input_last_name = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')
    input_delivery_address = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')
    input_metro_station = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    input_phone_number = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')
    btn_continue_to_rent = (By.XPATH, '//button[text()="Далее"]')
    metro_option_by_name = (By.XPATH, '//div[text()="{}"]')
    input_date = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')
    dropdown_rent_duration = (By.CLASS_NAME, 'Dropdown-placeholder')
    rent_option_one_day = (By.XPATH, '//div[text()="сутки"]')
    checkbox_color_black = (By.ID, 'black')
    checkbox_color_gray = (By.ID, 'grey')
    input_comment = (By.CSS_SELECTOR, '[placeholder="Комментарий для курьера"]')
    btn_submit_order = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]')
    modal_confirm_title = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    btn_confirm_yes = (By.XPATH, '//button[text()="Да"]')
