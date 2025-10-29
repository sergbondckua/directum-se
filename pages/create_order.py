from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base import BasePage


class CreateOrderPage(BasePage):
    """Створення замовлення."""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def press_btn_create(self):
        self.click(
            (
                By.XPATH,
                "//img[@src='images/create_3.4.2.0055.svg']/parent::div/parent::div",
            )
        )