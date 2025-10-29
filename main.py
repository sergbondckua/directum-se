import time

from drivers.browser import WebDriverSingleton
from pages.login import LoginPage

from environs import Env

# Читання змінних середовища
env = Env()
env.read_env()

driver = WebDriverSingleton.get_driver()  # отримання екземпляру драйвера

login_page = LoginPage(driver)  # ініціалізація сторінки авторизації
login_page.auth(env.str("USERNAME"), env.str("PASSWORD"))  # авторизація
time.sleep(15)

driver.quit()