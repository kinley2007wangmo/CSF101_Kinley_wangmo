def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

#  Example test cases
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 3, 4]
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print(containsDuplicate(nums1))  # True (1 repeats)
print(containsDuplicate(nums2))  # False (no duplicates)
print(containsDuplicate(nums3))  # True (many repeats)