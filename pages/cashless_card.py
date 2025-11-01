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
        pathname = "/path/to/file"
        self.typing((By.XPATH, "//input[@type='file']"), pathname)

    def type_document_field(self):
        """Заповнює поле Вид документа"""

        self.typing(
            (
                By.XPATH,
                "//label[text()='Вид документа']/parent::div/following-sibling::div//input[@role='combobox']",
            ),
            "Безналичный счет",
        )

    def curator_field(self):
        """Заповнює поле Куратор"""

        pass
