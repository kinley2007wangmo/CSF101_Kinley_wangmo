def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans

# Example test input
n = 5
print(countBits(n))  # Output: [0, 1, 1, 2, 1, 2]