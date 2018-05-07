# Write a function to calculate the minimum value in a list of integers.
# E.g. calc_min([1, 2, 3, 10, 7]) should return the value 1.

from sys import maxsize
def calc_min(numbers):
    current_min = maxsize
    for num in numbers:
        if num < current_min:
            current_min = num

    return current_min

calc_min([1, 2, 3, 10, 7])
