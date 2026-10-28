# calculator.py

class AdvancedCalculator:
    """Класс калькулятора с базовыми операциями и расширенной логикой."""

    def add(self, a, b):
        """Возвращает сумму двух чисел."""
        return a + b

    def divide(self, a, b):
        """Возвращает результат деления a на b. Вызывает ошибку при делении на ноль."""
        if b == 0:
            raise ValueError("Ошибка: Деление на ноль недопустимо!")
        return a / b

    def is_prime_number(self, n):
        """Проверяет, является ли целое число n простым."""
        if not isinstance(n, int):
            raise TypeError("Число должно быть целым")
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True