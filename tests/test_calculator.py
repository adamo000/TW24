import unittest
from pathlib import Path
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from screens.main_screen import MainScreen

class MyTestCase(unittest.TestCase):

    # before all
    @classmethod
    def setUpClass(cls):
        app_name = 'calculator.apk'
        app_path = str(Path(__file__).parent.parent.joinpath(app_name))
        appium_server_url = 'http://localhost:4723'
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.app = app_path
        cls.driver = webdriver.Remote(command_executor=appium_server_url, options=options)
        cls.main_screen = MainScreen(cls.driver)

    # before each
    def setUp(self):
        pass

    def test_add_2_values(self):
        self.main_screen.add_2_values(1, 2)
        result_preview = self.main_screen.get_result()
        self.assertEqual(int(result_preview), 3)

    # after each
    def tearDown(self):
        pass

    # after all
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
