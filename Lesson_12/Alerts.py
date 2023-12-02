from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://demoqa.com/alerts")
# Button_1 = ("xpath", "//button[@id='alertButton']")
# wait.until(EC.element_to_be_clickable(Button_1)).click()
#
# alert = wait.until(EC.alert_is_present())
# driver.switch_to.alert
# alert.accept()
Button_3 = ("xpath", "//button[@id='confirmButton']")
wait.until(EC.element_to_be_clickable(Button_3)).click()

alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
print(alert.text)
alert.dismiss()