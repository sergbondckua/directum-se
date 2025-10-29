import time

from drivers.browser import (
    FirefoxWebDriverFactory,
    WebDriverBrowser,
    ChromeWebDriverFactory,
)
from pages.login import LoginPage

from environs import Env

from utils.config import Config

# Читання змінних середовища
env = Env()
env.read_env()

config = Config()
factory = (
    FirefoxWebDriverFactory()
    if config.browser == "firefox"
    else ChromeWebDriverFactory()
)
with WebDriverBrowser(factory, config).get_driver() as driver:
    login_page = LoginPage(driver)  # ініціалізація сторінки авторизації
    login_page.auth(env.str("LOGIN"), env.str("PASSWORD"))  # авторизація
    time.sleep(15)
