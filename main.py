import time

from drivers.browser import (
    FirefoxWebDriverFactory,
    WebDriverBrowser,
    ChromeWebDriverFactory,
)
from pages.cashless_card import CashlessCard
from pages.create_order import CreateOrderPage
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
    # Авторизація
    login_page = LoginPage(driver)
    login_page.auth(env.str("LOGIN"), env.str("PASSWORD"))

    # Створення заявки
    create_order_page = CreateOrderPage(driver)
    create_order_page.creator()

    # Створення безготівкового рахунка
    cashless_card_page = CashlessCard(driver)
    # cashless_card_page.create_from_file()
    cashless_card_page.type_document_field()
    time.sleep(15)
