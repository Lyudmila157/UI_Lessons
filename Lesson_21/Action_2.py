from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get("https://demoqa.com/menu")

menu_item_2_locator = ("xpath", "//a[text()='Main Item 2']")
sub_list_locator = ("xpath", "//a[text()='SUB SUB lIST]")

menu_item_2 = driver.find_element(*menu_item_2_locator)
sub_list_menu = driver.find_element(*sub_list_locator)

action.move_to_element(menu_item_2) \
    .pause(2) \
    .move_to_element(sub_list_menu) \
    .perform()