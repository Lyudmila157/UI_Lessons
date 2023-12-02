from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

# driver.get("https://hyperskill.org/tracks")
#
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
#
# driver.get("https://ya.ru")

driver.switch_to.new_window("tab") # переключит на новую вкладку
driver.switch_to.new_window("tab") # переключит на новое окно
driver.get("https://ya.ru")