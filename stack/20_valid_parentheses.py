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
