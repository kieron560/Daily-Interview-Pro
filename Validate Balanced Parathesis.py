# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.

# Example:
# Input: "((()))"
# Output: True

# Input: "[()]{}"
# Output: True

# Input: "({[)]"
# Output: False


class Solution:
  def isValid(self, s): #Runtime = O(n) where n is length of string
    # Fill this in.
    count =[0,0,0]
    
    if s == "":
        return True

    while any(count) >= 0:
        for bracket in s:
            if bracket == "(":
                count[0] += 1
            if bracket == ")":
                count[0] -= 1
            if bracket == "[":
                 count[1] += 1
            if bracket == "]":
                 count[1] -= 1
            if bracket == "{":
                 count[2] += 1
            if bracket == "}":
                count[2] -= 1
    
        for i in count:
            if i != 0:
                return False
        return True

    return False

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))