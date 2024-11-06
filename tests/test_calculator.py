import unittest
from pathlib import Path
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


class MyTestCase(unittest.TestCase):

    def test_divide_by_zero(self):
        app_name = 'calculator.apk'
        app_path = str(Path(__file__).parent.parent.joinpath(app_name))
        appium_server_url = 'http://localhost:4723'

        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.app = app_path

        driver = webdriver.Remote(command_executor=appium_server_url, options=options)

        driver.find_element(AppiumBy.ACCESSIBILITY_ID, '2').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'divide').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, '0').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equals').click()
        result_preview = driver.find_element(AppiumBy.ID, 'result_preview').text

        self.assertEqual(result_preview, 'Can\'t divide by 0')

if __name__ == '__main__':
    unittest.main()
