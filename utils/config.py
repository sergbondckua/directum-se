from dataclasses import dataclass


@dataclass
class Config:
    """Клас конфігурації для додатку."""

    browser: str = "chrome"
    url: str = "https://site.com.ua"
    headless: bool = False
