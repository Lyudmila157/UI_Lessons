from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

#Локатор
form_name_field_locator = ("xpath", "//input[@id='RESULT_TextField-0']")
copy_text_locator = ("xpath", "//button[text()='Copy Text']")

#Основной скрипт
driver.get = ("https://testautomationpractice.blogspot.com/")
driver.switch_to.frame("frame-one796456169")

driver.switch_to.default_content()
driver.find_element(*form_name_field_locator).send_keys("Aleksey")
driver.find_element(*copy_text_locator).click()
