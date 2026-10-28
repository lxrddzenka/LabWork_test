# test_calculator.py
import pytest
from calculator import AdvancedCalculator


# Фикстура для создания объекта калькулятора перед каждым тестом
@pytest.fixture
def calc():
    return AdvancedCalculator()


# 1. Параметризованный тест для метода add
@pytest.mark.parametrize("a, b, expected", [
    (5, 5, 10),  # Два положительных
    (-3, -7, -10),  # Два отрицательных
    (-5, 10, 5),  # Отрицательное и положительное
    (0, 0, 0),  # Нули
    (2.5, 2.5, 5.0)  # Дробные числа
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


# 2. Параметризованный тест для успешного деления
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (-10, -2, 5),
    (5, 2, 2.5),
    (0, 5, 0)
])
def test_divide_success(calc, a, b, expected):
    assert calc.divide(a, b) == expected


# 3. Тест на проверку исключения при делении на ноль (Требование задания)
def test_divide_by_zero(calc):
    # Менеджер контекста pytest.raises перехватывает ожидаемую ошибку
    with pytest.raises(ValueError) as exception_info:
        calc.divide(10, 0)

    # Дополнительно можно проверить текст ошибки
    assert str(exception_info.value) == "Ошибка: Деление на ноль недопустимо!"


# 4. Параметризованный тест для метода is_prime_number
@pytest.mark.parametrize("number, is_prime", [
    (2, True),  # Минимальное простое число
    (3, True),  # Простое число
    (13, True),  # Простое число
    (97, True),  # Большое простое число
    (0, False),  # Ноль не является простым
    (1, False),  # Единица не является простым
    (4, False),  # Четное непростое
    (9, False),  # Нечетное непростое
    (-5, False)  # Отрицательное
])
def test_is_prime_number(calc, number, is_prime):
    assert calc.is_prime_number(number) == is_prime