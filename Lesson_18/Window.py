from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

#Локаторы
For_Business_Button_Locator = ("xpath", "//a[text()='For Business']")
Start_Free_Button_Locator = ("xpath", "//a[text()='Start for Free']")

driver.get("https://hyperskill.org/tracks")

# print(driver.window_handles)

# print(driver.current_window_handle)

driver.find_element(*For_Business_Button_Locator).click()

tabs = driver.window_handles
driver.switch_to.window(tabs[1])
driver.find_element(*Start_Free_Button_Locator).click()