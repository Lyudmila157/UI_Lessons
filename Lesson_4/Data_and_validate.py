import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://ru.wikipedia.org/")

# url = driver.current_url
# print("URL страницы", url)
# assert url == "https://ru.wikipedia.org/", "Ошибка в URL, открыта не страница"
#
# current_title = driver.title
# print("Текущий заголовок", current_title)
# assert current_title == "Википедия — свободная энциклопедия", "Некорректный заголовок"
print(driver.page_source)
time.sleep(3)