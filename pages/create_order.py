from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base import BasePage


class CreateOrderPage(BasePage):
    """Створення замовлення."""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def _press_on_btn_create(self):
        """Клік на кнопку створення задачі."""
        self.click(
            (
                By.XPATH,
                "//img[@src='images/create_3.4.2.0055.svg']/parent::div/parent::div",
            )
        )

    def _press_cashless_payment(self):
        """Клік на кнопку створення заявки на безготівкову оплату."""
        self.click(
            (By.CSS_SELECTOR, '[title="Создать заявка на безналичную оплату"]')
        )

    def _press_add_new_obj(self):
        """Клік на кнопку додавання нового об'єкту."""
        self.click(
            (
                By.XPATH,
                "//div[contains(@class, 'attachment-group__title') and text()='Заявка на безналичную оплату']/ancestor::div[@class='attachment-group attachments__attachment-group']//span[text()='Добавить']",
            )
        )

    def _press_create_new(self):
        self.click(
            (
                By.XPATH,
                "//img[@src='images/create_attachment_16_3.4.2.0055.svg']/parent::div",
            )
        )

    def creator(self):
        """Відкриває сторінку створення заявки на безготівкову оплату."""
        self._press_on_btn_create()
        self._press_cashless_payment()
        self._press_add_new_obj()
        self._press_create_new()