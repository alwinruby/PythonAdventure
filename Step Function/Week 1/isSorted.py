# Write a function to determine if a list of integers is sorted (strictly) in ascending order. 
# E.g. is_sorted([1, 2, 3, 10, 7]) should return False but is_sorted([1, 2, 3, 7, 10]) should return True.

def is_sorted(numbers):
    for ind in range(len(numbers) - 1):
        num = numbers[ind]
        next_num = numbers[ind + 1]
        if num >= next_num:
            return False

    return True

print(is_sorted([1, 2, 3, 10, 7]))
print(is_sorted([1, 2, 3, 7, 10]))
