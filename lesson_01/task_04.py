"""
4) Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.

Пример вывода:
Введите положительное целое число: 12383
Максимальная цифра: 8
"""

numbers = int(input("Введите положительное целое число: "))
numbers_temp = numbers
maximum_num: int = 0
while numbers_temp > 0:
    if numbers_temp % 10 > maximum_num:
        maximum_num = numbers_temp % 10
    numbers_temp //= 10
print(f"Максимальная цифра: {maximum_num}")
