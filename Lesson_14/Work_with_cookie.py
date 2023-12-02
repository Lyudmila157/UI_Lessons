import os
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/ru/ru/login")
driver.delete_all_cookies()
# login_field = ("xpath", "//input[@id='login_email']")
# password_field = ("xpath", "//input[@id='password']")
# submit_button = ("xpath", "//button[@id='loginformsubmit']")
#
# #Логинимся в аккаунт
# driver.get("https://www.freeconferencecall.com/ru/ru/login")
# driver.find_element(*login_field).send_keys("autocheck@ya.ru")
# driver.find_element(*password_field).send_keys("123")
# driver.find_element(*submit_button).click()
# pickle.dump(driver.get_cookies(), open(os.getcwd()+"/Cookies/cookies.pkl", "wb"))
cookies = pickle.load(open(os.getcwd()+"/Cookies/cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()