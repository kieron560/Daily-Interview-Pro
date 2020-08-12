# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# Here is the function signature as a starting point (in Python):

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:

  def addTwoNumbers(self, l1, l2, c = 0): #Runtime = O(n) where n is length of list
    # Fill this in.
    answer = ListNode(c) # Creates the answer linked list
    result = answer # pointer to the first node to be returned
    carry = 0

    while (l1 != None and l2 != None): 

        total = answer.val + l1.val + l2.val  
        answer.val = total % 10 
        carry =  int (total / 10) 
    
        if (l1.next == None and l2.next == None): # Reaching end of the lists
            if carry == 1:  
                answer.next = ListNode(carry)
        
        else:
            # If lists are of different length
            if (l1.next == None):
                l1.next = ListNode(0)

            if (l2.next == None):
                l2.next = ListNode(0)

            answer.next = ListNode(carry)
            answer = answer.next
            
        l1 = l1.next
        l2 = l2.next

    return result
   



l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val)
  result = result.next
# 7 0 8
