"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
"""
from operator import mul
from functools import reduce

print(reduce(mul, [number for number in range(100, 1001) if number % 2 == 0]))