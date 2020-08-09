# Given a string, find the length of the longest substring without repeating characters.
# Can you find a solution in linear time?


# For this particular problem, i have a really hard time visualising this solution
# So, pardon my excessive comments to explain to myself in a way that I can understand
# But from my understanding, it's the standard sliding window technique that uses more indexes to find in linear time


class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    start = 0 # Starting index of the string s
    result = 0 # Final Value we are returning
    length = len(s) # length of our string s 

    index = [-1] * 256 
    # this array of length 256 (number of ASCII characters) will hold the index of particular character of the string we are looping through, hence we set them as -1 initally

    for i in range(length): # Looping through the string, so i is the index of the "end" of the substring 

        # General rule, if you encounter consecutively same characters, use the latter character
        # "aab", we want to start counting from the second "a" etc.

        start = max(start, index[ord(s[i])] + 1) 
        # STEP 1
        # For the first character of the string, start = 0, because the value of index[ASCII of character of s[i]] = -1 + 1 = 0
        # Notice that because of the third line in the for loop, all new characters in index will be -1 unless encountered.
        # Hence, start will not change until you encounter the same character again.
        
        # STEP 4
        # When you encounter, you automatically increment the start by 1 (since index[ord(s[i])] + 1), which automatically makes the next index the start of the window

        result = max(result, i - start + 1)
        # STEP 2
        # result is the max of result (since we want the longest substring), or i - start + 1
        # i - start + 1 is the current length of the window (i is the "end" of the window and start is the "start" of the window)

        # STEP 5
        # Now with a new starting point, you can compare the new windows (with a new starting point aka the next index) with old windows (using the prev index as start)
        # Hence, if there is a longer window that we have found before, we use it
        # All this is done behind the scenes concurrently in linear time as the "end" of the window aka i loops linearly anyway

        index[ord(s[i])] = i
        # STEP 3
        # We set the value of index[ASCII of character of s[i]] = i, so as to track the last index of each letter in the index array
        
    return result

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10



# EXAMPLE "aab", result = 2
# first "a", start = 0, result = 1, index["a"] = 0
# second "a", start = 1, result = 1 (1-1+1), index["a"] = 1
# third "b", start = 1 (since 1 > 0), result = 2 (2-1+1), index["b"] = 0

# EXAMPLE "abrkacd", result = 6
# for the first "abrk", result = 4, start = 0 (since theres no repeating characters), all the respective index[characters] = i
# then, "abrka", start = 1, result = 4, index["a"] = 4, the rest = i (1,2,3 respectively)
# Notice now that we have a repeating character, start automatically increments by 1 to start from "b"
# The process goes on and on, and since there's no more repeating character, start = 1 etc.

