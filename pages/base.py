from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger import log_action


class BasePage:
    """Базова сторінка."""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @log_action
    def open(self, url: str):
        """
        Відкриття веб-сторінки.

        Args:
            url (str): URL веб-сторінки.
        """

        self.driver.get(url)

    @log_action
    def find(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        """
        Пошук елемента на сторінці.

        Args:
            locator (tuple[str, str]): Локатор елемента.
            timeout (int, optional): Час очікування. Defaults to 5.

        Returns:
            WebElement: Елемент, що був знайдений.
        """
        # Очікуємо елемент на сторінці
        return WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(locator)
        )

    @log_action
    def find_all(self, locator: tuple[str, str]):
        return self.driver.find_elements(*locator)

    @log_action
    def click(self, locator: tuple[str, str]):
        """
        Клік на елемент.

        Args:
            locator (tuple[str, str]): Локатор елемента.
        """
        # Очікуємо елемент на сторінці
        element = self.find(locator)
        # Клік на елемент
        element.click()

    @log_action
    def typing(self, locator: tuple[str, str], text: str):
        """
        Введення тексту.

        Args:
            locator (tuple[str, str]): Локатор елемента, у який буде вставлений текст.
            text (str): Текст, що буде вставлений.
        """
        # Очікуємо елемент на сторінці
        element = self.find(locator)
        # Введення тексту
        element.send_keys(text)
