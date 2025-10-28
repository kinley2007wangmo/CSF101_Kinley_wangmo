def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    char_counts = [0] * 26
    
    for c1, c2 in zip(s, t):
        char_counts[ord(c1) - ord('a')] += 1
        char_counts[ord(c2) - ord('a')] -= 1
    
    return all(count == 0 for count in char_counts)

# Example test input
s = "anagram"
t = "nagaram"
print(isAnagram(s, t))  # Output: True
