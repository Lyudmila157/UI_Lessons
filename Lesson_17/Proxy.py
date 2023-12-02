from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Proxy_server = "37.19.220.129:8443"
# options = Options()
# options.add_argument(f"--proxy-server={Proxy_server}")
# driver = webdriver.Chrome()
# driver.get("https://2ip.ru")

Proxy_server = "username:password@37.19.220.129:8443"
options = Options()
options.add_argument(f"--proxy-server={Proxy_server}")
driver = webdriver.Chrome()
driver.get("https://2ip.ru")

