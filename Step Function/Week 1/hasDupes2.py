# Use Python set to solve if a list of integers contains any duplicates.
#E.g. has_dupes([1, 2, 3, 10, 7]) should return False but has_dupes([1, 2, 3, 10, 10]) should return True.

def has_dupes(numbers):
    return len(numbers) != len(set(numbers))

print(has_dupes([1, 2, 3, 10, 7]))
print(has_dupes([1, 2, 3, 10, 10]))

my_list = [1, 2, 3, 10, 10]
set(my_list)
