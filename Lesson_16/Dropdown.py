from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

select_locator = ("xpath", "//select[@id='dropdown']")
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = Select(driver.find_element(*select_locator))

# dropdown.select_by_visible_text("Option")
# dropdown.select_by_value("2")
# dropdown.select_by_index("1")

all_options = dropdown.options
# print(all_options)
# for option in all_options:
#     if "Option 1" in option.text:
#         print("Опция присутствует")
#     # dropdown.select_by_visible_text(option.text)

# for option in all_options:
#     dropdown.select_by_index(all_options.index(option))
#
for option in all_options:
    dropdown.select_by_value(option.get_attribute("value"))