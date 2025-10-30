from dataclasses import dataclass, field
from typing import List


@dataclass
class Config:
    """Клас конфігурації для додатку."""

    browser: str = "chrome"
    url: str = "https://drx.const.dp.ua"
    headless: bool = False
    chrome_args_options: List[str] = field(default_factory=lambda: [
        "--no-sandbox",
        "--ignore-certificate-errors",
        "--ignore-ssl-errors",
        "--allow-insecure-localhost",
        "--allow-running-insecure-content",
        "--ignore-certificate-errors-spki-list",
        "--disable-web-security",
    ])
    firefox_args_options: List[str] = field(default_factory=lambda: [
        "--no-sandbox",
        "--allow-running-insecure-content",
    ])

    firefox_prefs: dict = field(default_factory=lambda: {
        "network.stricttransportsecurity.preloadlist": False,
        "security.enterprise_roots.enabled": True,
        "security.mixed_content.block_active_content": False,
        "security.mixed_content.block_display_content": False,
        "webdriver_accept_untrusted_certs": True,
        "webdriver_assume_untrusted_issuer": False,
    })


