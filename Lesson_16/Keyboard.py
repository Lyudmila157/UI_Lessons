from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

keyboard_input = ("xpath", "//input[@id='target']")
driver.get("https://the-internet.herokuapp.com/key_presses")
# driver.find_element(*keyboard_input).send_keys(Keys)
# driver.find_element(*keyboard_input).send_keys("hdkfhkseh")
# driver.find_element(*keyboard_input).send_keys(Keys.CONTROL + "A")

# select_locator = ("xpath", "//input[@id='react-select-3-input']")
# driver.get("https://demoqa.com/select-menu")
# driver.find_element(*select_locator).send_keys("Ms.")
# driver.find_element(*select_locator).send_keys(Keys.ENTER)

multiselect_locator = ("xpath", "//input[@id='react-select-4-input'")
driver.get("https://demoqa.com/select-menu")
driver.find_element(*multiselect_locator).send_keys("Green")
driver.find_element(*multiselect_locator).send_keys(Keys.ENTER)
driver.find_element(*multiselect_locator).send_keys("Blue")
driver.find_element(*multiselect_locator).send_keys(Keys.ENTER)