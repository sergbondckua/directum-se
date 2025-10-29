from abc import ABC, abstractmethod

from selenium import webdriver
from utils.config import Config


class WebDriverFactory(ABC):
    """Фабрика для створення WebDriver."""

    @abstractmethod
    def create_driver(self, config: Config) -> webdriver.Remote:
        """Створення WebDriver."""
        pass


class ChromeWebDriverFactory(WebDriverFactory):
    """Фабрика для створення Chrome WebDriver."""

    def create_driver(self, config: Config) -> webdriver.Chrome:
        """Створення Chrome WebDriver."""

        options = webdriver.ChromeOptions()
        if config.headless:
            options.add_argument("--headless=new")

        # Додаткові Chrome аргументи
        for argument in config.chrome_args_options:
            options.add_argument(argument)

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver


class FirefoxWebDriverFactory(WebDriverFactory):
    """Фабрика для створення Firefox WebDriver."""

    def create_driver(self, config: Config) -> webdriver.Firefox:
        """Створення Firefox WebDriver."""

        options = webdriver.FirefoxOptions()
        if config.headless:
            options.add_argument("--headless")

        # Додаткові Firefox аргументи
        for arg in config.firefox_args_options:
            options.add_argument(arg)

        for key, value in config.firefox_prefs.items():
            options.set_preference(key, value)

        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver


class WebDriverBrowser:
    """Управління WebDriver."""

    def __init__(self, factory: WebDriverFactory, config: Config):
        self.config = config
        self.factory = factory
        self.driver = None

    def __enter__(self):
        self.get_driver()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit_driver()

    def get_driver(self) -> webdriver.Remote:
        """Екземпляр драйвера"""
        return self.factory.create_driver(self.config)

    def quit_driver(self):
        """Закрити драйвер"""
        if self.driver:
            self.driver.quit()
