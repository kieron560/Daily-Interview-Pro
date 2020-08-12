# Input: "banana"
# Output: "anana"

# Input: "million"
# Output: "illi"

class Solution: 
    def longestPalindrome(self, s): #Runtime = O(n^2) where n is length of string
      # Fill this in.
      result = ""
      
      for i in range(len(s)):
          for j in range(len(s) + 1):
            current = s[i:j]
            if current == current[::-1]:
                if len(current) > len(result):
                    result = current
                    
      return result

        
# Test program
# s = "tracecars"
# s= "aaa"
s = "million"
print(str(Solution().longestPalindrome(s)))
# racecar