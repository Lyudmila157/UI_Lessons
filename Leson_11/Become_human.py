from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--headless")
options.add_argument("--windows-size=1920.1080")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)
#
# driver.get("https://www.youtube.com/watch?v=0lM3RdR1ATk")
# driver.get_screenshot_as_file("screen.png")

driver.get("https://whatismyipaddress.com/")

wait.until(EC.title_is("What Is My IP Address - See Your Public Address - IPv4 & IPv6"))
driver.get_screenshot_as_file("screening.png")


