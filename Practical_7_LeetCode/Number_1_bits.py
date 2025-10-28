def hammingWeight(n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

# Example test input
n = 11  # Binary representation: 1011
print(hammingWeight(n))  # Output: 3
