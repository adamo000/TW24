from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class MainScreen:

    # static selector
    __result_final_selector = (AppiumBy.ID, 'result_final')
    __add_operator_selector = (AppiumBy.CSS_SELECTOR, '[resource-id="op_add"]')
    __equals_selector = (AppiumBy.XPATH, '//*[@content-desc="equals"]')
    __history_result_selector = (AppiumBy.ID, 'history_result')
    __handler_selector = (AppiumBy.ID, 'drag_handle_view')
    __point_selector = (AppiumBy.ACCESSIBILITY_ID, 'point')

    # dynamic selector
    __digit_strategy_selector = AppiumBy.ACCESSIBILITY_ID

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def add_2_values(self, value1, value2):
        self.driver.find_element(self.__digit_strategy_selector, str(value1)).click()
        self.driver.find_element(*self.__add_operator_selector).click()
        self.driver.find_element(self.__digit_strategy_selector, str(value2)).click()
        self.driver.find_element(*self.__equals_selector).click()

    def get_result(self):
        result = self.driver.find_element(*self.__result_final_selector).text
        return result

    def expand_history(self):
        start_handler = self.driver.find_element(*self.__handler_selector)
        end_handler = self.driver.find_element(*self.__point_selector)
        self.driver.scroll(start_handler, end_handler)

    def get_history_result(self):
        result = self.driver.find_element(*self.__history_result_selector).text
        return result