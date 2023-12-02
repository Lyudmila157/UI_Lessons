from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# checkbox_home_status = ("xpath", "//input[@id='tree-node-home']")
# checkbox_home_action = ("xpath", "//span[@class='rtc-checkbox']")
# driver.get("https://demoqa.com/checkbox")
#
# # print(driver.find_element(*checkbox_1).is_selected())
# # driver.find_element(*checkbox_1).click()
# # print(driver.find_element(*checkbox_1).is_selected())
#
# print(driver.find_element(*checkbox_home_status).is_selected())
# driver.find_element(*checkbox_home_action).click()
# print(driver.find_element(*checkbox_home_status).is_selected())

# element_one = ("xpath", "//ili[text()='Cras justo odio']")
# driver.get("https://demoqa.com/selectable")
# before = driver.find_element(*element_one).get_attribute("class")
# print(before)
# driver.find_element(*element_one).click()
# after = driver.find_element(*element_one).get_attribute("class")
# print(after)
# assert "active" in after

yes_radio_status = ("xpath", "//input[@id='yesRadio']")
yes_radio_action = ("xpath", "//label[@for='yesRadio']")

no_radio_status = ("xpath", "//input[@id='noRadio']")
no_radio_action = ("xpath", "//label[@for='noRadio']")

driver.get("https://demoqa.com/radio-button")

print(driver.find_element(*yes_radio_status).is_selected())
driver.find_element(*yes_radio_action).click()
print(driver.find_element(*yes_radio_status).is_selected())