from pathlib import Path
from appium import webdriver 
from appium.options.android import UiAutomator2Options

app_name = "calculator.apk"
app_path = str(Path(__file__).parent.joinpath(app_name))
appium_server_url = 'http://localhost:4723'

options = UiAutomator2Options() 
options.platform_name = "Android" 
options.app = app_path

driver = webdriver.Remote(command_executor=appium_server_url, options=options)
