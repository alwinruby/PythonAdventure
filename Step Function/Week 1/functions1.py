# Write a function to count how many even numbers there are in a list of integers.
#E.g. count_evens([1, 2, 3, 10, 7]) should return the value 2.

def count_evens(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1

    return count

count_evens([1, 2, 3, 10, 7])
