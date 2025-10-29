from selenium.webdriver.common.by import By

from pages.base import BasePage
from utils.config import Config


class LoginPage(BasePage):
    """Клас сторінки авторизації."""

    USERNAME = (By.ID, "login-user-id")
    PASSWORD = (By.ID, "login-password-id")
    LOGIN_BUTTON = (By.CLASS_NAME, "login__submit-button")

    def __init__(self, driver):
        super().__init__(driver)

    def _open_login_page(self):
        """Відкриття сторінки авторизації."""
        self.open(Config().url)

    def _typing_username(self, username: str):
        """Введення логіну."""
        self.typing(self.USERNAME, username)

    def _typing_password(self, password: str):
        """Введення паролю."""
        self.typing(self.PASSWORD, password)

    def _click_login_button(self):
        """Клік на кнопку авторизації."""
        self.click(self.LOGIN_BUTTON)

    def auth(self, username: str, password: str):
        """Авторизація."""
        self._open_login_page()
        self._typing_username(username)
        self._typing_password(password)
        self._click_login_button()
