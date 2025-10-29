import time

from drivers.browser import WebDriverSingleton
from pages.login import LoginPage

driver = WebDriverSingleton.get_driver()

login_page = LoginPage(driver)
login_page.auth("user", "passwd")
time.sleep(10)

driver.quit()