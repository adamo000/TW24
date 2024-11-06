from pathlib import Path
from appium import webdriver 
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

app_name = 'calculator.apk'
app_path = str(Path(__file__).parent.joinpath(app_name))
appium_server_url = 'http://localhost:4723'

options = UiAutomator2Options() 
options.platform_name = 'Android'
options.app = app_path

driver = webdriver.Remote(command_executor=appium_server_url, options=options)



driver.find_element(AppiumBy.ACCESSIBILITY_ID, '2').click()
driver.find_element(AppiumBy.CSS_SELECTOR, '[resource-id="op_add"]').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, '1').click()
driver.find_element(AppiumBy.XPATH, '//*[@content-desc="equals"]').click()

result = driver.find_element(AppiumBy.ID, 'result_final').text

assert int(result) == 3, f'Error: {result} is not 3'
