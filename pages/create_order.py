from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base import BasePage


class CreateOrderPage(BasePage):
    """Створення замовлення."""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def press_on_btn_create(self):
        """Клік на кнопку створення задачі."""
        self.click(
            (
                By.XPATH,
                "//img[@src='images/create_3.4.2.0055.svg']/parent::div/parent::div",
            )
        )

    def press_cashless_payment(self):
        """Клік на кнопку створення заявки на безготівкову оплату."""
        self.click(
            (By.CSS_SELECTOR, '[title="Создать заявка на безналичную оплату"]')
        )

    def press_add_new_obj(self):
        """Клік на кнопку додавання нового об'єкту."""
        attachments = self.find((By.ID, "attachments"))

        add_btn = attachments.find_elements(By.TAG_NAME, "div")[2]
        print(add_btn.text)
        add_btn.click()

    def press_create_new(self):
        self.click((By.XPATH, "//*[@title='Создать новый объект']"))
