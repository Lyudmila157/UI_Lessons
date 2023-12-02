from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

Login_field = ("xpath", "//input[@type='email']")
Password_field = ("xpath", "//input[@type='password']")
Submit_button = ("xpath", "//button[@type='submit']")

driver.get("https://hyperskill.org/login")
driver.find_element(*Login_field).send_keys("alekseyk@ya.ru")
driver.find_element(*Password_field).send_keys("Qwerty132!")
driver.find_element(*Submit_button).click()

driver.switch_to.new_window("window")