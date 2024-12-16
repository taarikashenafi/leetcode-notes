# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

# Approach: Stack using Deque
# To solve this problem, we can use a stack to keep track of the opening brackets as we iterate over the input string.
# We can use a mapping dictionary to map closing brackets to their corresponding opening brackets.
# If we encounter a closing bracket, we check if there's an opening bracket on the stack and it matches the closing bracket.
# If it matches, we pop the opening bracket from the stack. If it doesn't match or the stack is empty, the string is not valid.
# If we encounter an opening bracket, we push it onto the stack.
# Finally, if the stack is empty, all opening brackets have been matched; return True. If the stack is not empty, there are unmatched opening brackets; return False.

# Time complexity: O(n), where n is the length of the input string s.
# Space complexity: O(n), where n is the length of the input string s.


from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Initialize a deque to use as a stack for tracking opening brackets
        chars = deque()
        # Define a mapping for closing brackets to their corresponding opening brackets
        char_map = {')': '(', ']': '[', '}': '{'}

        # Iterate over each character in the input string
        for char in s:
            # If the character is a closing bracket
            if char in char_map:
                # Check if there's an opening bracket on the stack and it matches the closing bracket
                if chars and chars[-1] == char_map[char]:
                    # If it matches, pop the opening bracket from the stack
                    chars.pop()
                else:
                    # If it doesn't match or stack is empty, the string is not valid
                    return False
            else:
                # If the character is an opening bracket, push it onto the stack
                chars.append(char)
        
        # If the stack is empty, all opening brackets have been matched; return True
        # If the stack is not empty, there are unmatched opening brackets; return False
        return not chars

