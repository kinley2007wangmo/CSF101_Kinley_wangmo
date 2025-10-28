def isValid(s):
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in bracket_map:  # it's a closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:  # it's an opening bracket
            stack.append(char)
    
    return len(stack) == 0

# Example test input
s = "()[]{}"
print(isValid(s))  # Output: True