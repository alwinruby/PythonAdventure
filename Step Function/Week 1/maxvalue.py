# Write a function to calculate the maximum value in a list of integers.
# E.g. calc_max([1, 2, 3, 10, 7]) should return the value 10.

from sys import maxsize
def calc_max(numbers):
    current_max = -maxsize
    for num in numbers:
        if num > current_max:
            current_max = num

    return current_max

calc_max([1, 2, 3, 10, 7])
