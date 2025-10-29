import logging
from typing import Callable

# Налаштування логів
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger("selenium-logger")


def log_action(func: Callable) -> Callable:
    """Декоратор для логування дій."""

    def wrapper(self, *args, **kwargs):
        logger.info(f"{str(func.__name__).upper()} called with args={args} kwargs={kwargs}")
        return func(self, *args, **kwargs)

    return wrapper
