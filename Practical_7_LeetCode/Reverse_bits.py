def reverseBits(n):
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
 
# Example test input
n = 43261596  # Binary representation: 00000010100101000001111010011100
print(reverseBits(n))  # Output: 964176192 (Binary representation: 00111001011110000010100101000000)