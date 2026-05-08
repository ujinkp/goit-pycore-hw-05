from typing import Callable


def generator_numbers(text: str):
    for part in text.split():
        try:
            yield float(part) # Сапроба перетворити не число
        except ValueError:
            # Ігноруємо якщо не число
            continue


def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}") #Загальний дохід: 1351.46