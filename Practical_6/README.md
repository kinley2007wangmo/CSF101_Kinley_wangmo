# Practical 6

## Overview

- This Python program demonstrates three common searching algorithms used in data structures and algorithms:

1. Linear Search
2. Binary Search
3. Recrusive Binary Search

- Each function searches for a specific value (target) in a list of numbers and returns the index of the target if found, or -1 if not found.

## Algorithms Explained

1. ### Linear Search
- The simplest searching algorithm.
- It scans each element of the list one by one until it finds the target value.
- Does not require the list to be sorted.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


#### Example Output:
Linear Search: Index of 6 is 7

2. ### Binary Search
- A faster search algorithm but works only on sorted lists.
- It repeatedly divides the search range in half until the target is found.
- Uses a while loop to perform the search iteratively.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


#### Example Output:
Binary Search: Index of 6 in sorted list is 8

3. ### Recrusive Binary Search
- The recursive version of binary search.
- Instead of using loops, it calls itself repeatedly with a smaller range until the target is found.

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


#### Example Output:
Recursive Binary Search: Index of 6 in sorted list is 8

### Test Data
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
target = 6

- Linear Search works on test_list directly.
- Binary Search uses a sorted version of the same list.

## Conclusion
- Linear Search is easy to implement but inefficient for large datasets.
- Binary Search (both iterative and recursive) is much faster but requires a sorted list.