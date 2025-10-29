from selenium import webdriver
from utils.config import Config


class WebDriverSingleton:
    """Клас Singleton для WebDriver."""

    _driver = None

    @classmethod
    def get_driver(cls, config: Config = None) -> webdriver.Chrome:
        """Отримання екземпляру WebDriver."""
        if cls._driver is None:
            if config is None:
                config = Config()

            options = webdriver.ChromeOptions()
            if config.headless:
                options.add_argument("--headless")

            cls._driver = webdriver.Chrome(options=options)
            cls._driver.maximize_window()
            cls._driver.implicitly_wait(10)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        """Закриття драйвера."""
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
