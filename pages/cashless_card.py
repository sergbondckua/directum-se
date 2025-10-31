from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base import BasePage


class CashlessCard(BasePage):
    """Сторінка безготівковий рахунок."""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def create_from_file(self):
        """Додавання файлу рахунка"""

        # self.click(
        #     (
        #         By.XPATH,
        #         "//span[contains(@class, 'ribbon-item__text') and text()='Создать из файла']",
        #     )
        # )
        file = self.find((By.XPATH, "//input[@type='file']"))
        file.send_keys("/path/to/file")
