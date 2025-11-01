import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base import BasePage


class CashlessCard(BasePage):
    """Сторінка безготівковий рахунок."""

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    # Функція для заповнення dropdown (combobox)
    def fill_dropdown(
        self, label: str, value: str, clickable: bool = True, timeout: int = 2
    ):
        """Заповнює будь-який dropdown за label.
        Якщо clickable=False — працює з не клікабельним combobox.
        """
        input_type = (
            "contains(@class, 'lookup-input_clickable')"
            if clickable
            else "@role='combobox'"
        )
        xpath = (
            f"//label[text()='{label}']"
            f"/parent::div/following-sibling::div"
            f"//input[{input_type}]"
        )
        element = self.find((By.XPATH, xpath))
        time.sleep(0.5)
        element.send_keys(value)
        # Чекаємо появи випадаючого списку і вибираємо перший варіант
        time.sleep(1.5)
        element.send_keys(Keys.ENTER)
        time.sleep(timeout)

    # Функція для заповнення текстових полів
    def fill_text_field(self, label, value):
        """Заповнює поле текстовим значенням"""
        xpath = (
            f"//label[text()='{label}']"
            f"/parent::div/following-sibling::div//input[@type='text']"
        )
        self.typing((By.XPATH, xpath), value)

    def _create_from_file(self):
        """Додавання файлу рахунка"""
        pathname = "/path/to/file"
        self.typing((By.XPATH, "//input[@type='file']"), pathname)

    def _type_document_field(self):
        """Заповнює поле Вид документа"""
        self.fill_dropdown("Вид документа", "Безналичный счет")

    def _curator_field(self):
        """Заповнює поле Куратор"""
        self.fill_dropdown("Куратор", "----")

    def _business_field(self):
        """Заповнює поле Бізнес"""
        self.fill_dropdown("Бизнес", "Телекоммуникационный")

    def _legal_entity_payer_field(self):
        """Заповнює поле Юр. особа"""
        self.fill_dropdown("Юр. лицо (плательщик)", 'ТОВ "ІНТРА.КОМ"')

    def _legal_entity_recipient_field(self):
        """Заповнює поле Юр. особа"""
        self.fill_dropdown(
            "Юр. лицо (получатель)", "Спортек-Черкаси", False
        )

    def _order_field(self):
        """Заповнює поле Рахунок №"""
        self.fill_text_field("Счет №", "12345")

    def creator(self):
        # self._create_from_file()
        self._type_document_field()
        self._curator_field()
        self._business_field()
        self._legal_entity_payer_field()
        self._legal_entity_recipient_field()
        self._order_field()
