from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url: str):
        """Відкриття веб-сторінки."""
        self.driver.get(url)

    def find(self, locator: tuple[str, str], timeout: int = 5) -> WebElement:
        """Пошук елемента."""
        return WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(locator)
        )

    def click(self, locator: tuple[str, str]):
        """Клік на елемент."""
        self.find(locator).click()

    def typing(self, locator: tuple[str, str], text: str):
        """Введення тексту."""
        self.find(locator).send_keys(text)