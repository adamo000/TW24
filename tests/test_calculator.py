import unittest
from appium.webdriver.appium_service import AppiumService

from screens.main_screen import MainScreen

from helpers.appium_manager import get_driver

class MyTestCase(unittest.TestCase):

    # before all
    @classmethod
    def setUpClass(cls):
        cls.appium_service = AppiumService()
        cls.appium_service.start()
        cls.driver = get_driver()
        cls.main_screen = MainScreen(cls.driver)

    # before each
    def setUp(self):
        pass

    def test_add_2_values(self):
        self.main_screen.add_2_values(1, 2)
        result_preview = self.main_screen.get_result()
        self.assertEqual(int(result_preview), 3)

    def test_add_2_values_zeros(self):
        self.main_screen.add_2_values(0, 0)
        result_preview = self.main_screen.get_result()
        self.assertEqual(int(result_preview), 0)

    def test_expand_history(self):
        self.main_screen.add_2_values(1, 9)
        self.main_screen.expand_history()
        history_result_review = self.main_screen.get_history_result()
        self.assertEqual(int(history_result_review), 10)

    # after each
    def tearDown(self):
        self.driver.execute_script('mobile: clearApp', {'appId': 'com.google.android.calculator'})
        self.driver.activate_app('com.google.android.calculator')

    # after all
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.appium_service.stop()


if __name__ == '__main__':
    unittest.main()
