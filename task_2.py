import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r'\b\d+\.?\d*\b'
    for match in re.finditer(pattern, text):
        number_str = match.group(0)
        try:
            yield float(number_str)
        except ValueError:
            print(f"Помилка перетворення числа: {number_str}")

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    total_sum = 0.0
    for number in func(text):
        total_sum += number
    return total_sum

# Приклад використання
# Загальний дохід: 1351.46
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

# Додатковий приклад
text_2 = "Зарплата: 1500.50. Премія: 250.00. Бонус: 50. Аванс: 100.25."
total_income_2 = sum_profit(text_2, generator_numbers)
print(f"Загальний дохід 2: {total_income_2}")
