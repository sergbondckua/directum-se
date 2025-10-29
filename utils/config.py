from dataclasses import dataclass, field
from typing import List


@dataclass
class Config:
    """Клас конфігурації для додатку."""

    browser: str = "chrome"
    url: str = "https://drx.const.dp.ua"
    headless: bool = False
    arguments_options: List[str] = field(default_factory=lambda: [
        "--no-sandbox",
        "--ignore-certificate-errors",
        "--ignore-ssl-errors",
        "--allow-insecure-localhost",
        "--allow-running-insecure-content",
        "--ignore-certificate-errors-spki-list",
        "--disable-web-security",
    ])

