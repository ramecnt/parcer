import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key: str = os.getenv('API_KEY')


def get_all_exchange_rates(src: str) -> dict:
    """Получает все обменные курсы для указанной валюты."""
    data = requests.get(f'https://open.er-api.com/v6/latest/{src}').json()
    if data["result"] == "success":
        exchange_rates = data["rates"]
        return exchange_rates


def convert_currency(amount: float, currency: str, new_currency: str) -> int:
    """Конвертирует сумму из одной валюты в другую."""
    if currency == 'RUR':
        currency = 'RUB'
    if new_currency == 'RUR':
        new_currency = 'RUB'
    exchange_rates = get_all_exchange_rates(currency)
    if exchange_rates:
        return int(exchange_rates[new_currency] * amount)


def is_supported_currency(currency: str) -> bool:
    """Проверяет, поддерживается ли указанная валюта."""
    return (currency in get_all_exchange_rates("USD") or currency == "USD")
