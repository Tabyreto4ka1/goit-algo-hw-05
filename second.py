from typing import Callable
import re


def generator_numbers(text: str):
    pattern=r"\b\d+(?:\.\d+)?\b"         # Патерн для пошуку доходу
    for match in re.finditer(pattern, text): # для  match шукаємо дохід в тексті за патернном 
        yield float(match.group())         # Повертаємо але не зупиняємо функцію. Також перетворюємо дохід у float
def sum_profit(text: str, func: Callable):
    summa=sum(func(text)) # Суммуємо все, що нам дає функція generator_numbers
    return summa


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")