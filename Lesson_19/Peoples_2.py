from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
user_1 = webdriver.Chrome(options=options)

Login_field = ("xpath", "//input[@type='email']")
Password_field = ("xpath", "//input[@type='password']")
Submit_button = ("xpath", "//button[@type='submit']")

user_1.get("https://hyperskill.org/login")
user_1.find_element(*Login_field).send_keys("alekseyk@ya.ru")
user_1.find_element(*Password_field).send_keys("Qwerty132!")
user_1.find_element(*Submit_button).click()

user_2 = webdriver.Chrome(options=options)
user_2.get("https://hyperskill.org/login")