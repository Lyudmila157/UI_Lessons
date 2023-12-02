from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

left_click_button_locator = ("xpath", "//button[@id='leftClick']")
double_click_button_locator = ("xpath", "//button[@id='doubleClick']")
right_click_button_locator = ("xpath", "//button[@id='rightClick']")
hover_button_locator = ("xpath", "//button[@id='colorChangeOnHover']")

driver.get("https://testkru.com/Elements/Buttons")

left_button = driver.find_element(*left_click_button_locator)
double_button = driver.find_element(*double_click_button_locator)
right_button = driver.find_element(*right_click_button_locator)
hover_button = driver.find_element(*hover_button_locator)

action.move_to_element(hover_button).perform()
