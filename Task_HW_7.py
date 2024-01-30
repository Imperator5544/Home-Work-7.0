# """
# Завдання 1.
#
# Написати рекурсивну функцію знаходження ступеня числа.
# """
#
# def get_number_pow(number, number_pow):
#     if number_pow <= 1:
#         return number
#     return number * get_number_pow(number, number_pow - 1)
# print(get_number_pow(5,4))


# """
# Завдання 2.
#
# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
#
# Проілюструйте роботу функції прикладом. (Протестувати)
# """
#
# def print_stars(n):
#     if n <= 0:
#         return
#     print('*', end='')
#     print_stars(n - 1)
#
# try:
#     n = int(input("Enter number of stars (integer): "))
#     print_stars(n)
# except ValueError:
#     print("Please enter an integer.")


# """
# Завдання 3.
#
# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
#
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.
# """
#
# def sum_range(a, b):
#     if a > b:
#         return 0
#     return a + sum_range(a +1, b)
#
# try:
#     a = int(input("Enter the value a:"))
#     b = int(input("Enter the value b:"))
#     result = sum_range(a, b)
#     print(f"Sum of numbers in the range {a} to {b}: {result}")
# except ValueError:
#     print("Please enter integer value")

"""
Завдання 4.

Напишіть рекурсивну функцію,
яка приймає одновимірний масив із 100 цілих чисел заповнених випадковим чином і знаходить позицію,
з якої починається послідовність із 10 чисел, сума яких мінімальна.
"""

import random
import math

import random
import math

def find_min_sum_index(numbers, start_index, end_index, min_sum=math.inf, min_index=0):
    if end_index < len(numbers):
        current_sum = sum(numbers[start_index:end_index + 1])
        if current_sum < min_sum:
            min_sum = current_sum
            min_index = start_index
        start_index += 1
        end_index += 1
        print(f"Current sum: {current_sum} Min sum {min_sum} Min_index: {min_index}")

        return find_min_sum_index(numbers, start_index, end_index, min_sum, min_index)

    return min_index

nums = [random.randint(1, 10) for _ in range(100)]
print(nums)
result = find_min_sum_index(nums, 0, 9)
print(result)