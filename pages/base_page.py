from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_on_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def find_element_with_wait(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    def switch_to_last_tab(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def wait_for_url(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(expected_url))
