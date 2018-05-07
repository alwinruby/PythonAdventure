# Write a function to determine if a list of integers contains any duplicates.
# E.g. has_dupes([1, 2, 3, 10, 7]) should return False but has_dupes([1, 2, 3, 10, 10]) should return True.


my_list = [1, 2, 5, 4, 5, 6, 7]
# Go through the list, one element at a time. Compare this element
# against every element before it. If it's in this set, we have a dupe;
# otherwise continue.
def has_dupes(numbers):
    for ind, num in enumerate(numbers):
        if num in numbers[:ind]:
            return True

    return False

print(has_dupes([1, 2, 3, 10, 7]))
print(has_dupes([1, 1, 2, 2, 10, 10]))
