from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
action = ActionChains(driver)

#Вариант 1
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
#
# column_A = ("xpath", "//div[@id=''column-a]")
# column_B = ("xpath", "//div[@id=''column-b]")
#
# A = driver.find_element(*column_A)
# B = driver.find_element(*column_B)
#
# action.drag_and_drop(A, B).perform()

#Вариант 2
driver.get("https://tympanus.net/Development/DragDropInteractions/sidebar.html")

grid_item = ("xpath", "(//div[@class='grid__item'])[3]")
sidebar_item = ("xpath", "(//div[@class='drop-area__item'])[3]")
action.click_and_hold(driver.find_element(*grid_item)) \
    .pause(1,5) \
    .move_to_element(driver.find_element(*sidebar_item)) \
    .release() \
    .perform()
