# Using the previous two functions, write a function to calculate the difference between the largest and smallest value in a list of integers.
# E.g. calc_range([1, 2, 3, 10, 7]) should return the value 9.

def calc_range(numbers):
    return calc_max(numbers) - calc_min(numbers)

calc_range([1, 2, 3, 10, 7])
