# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Clarification:
# - Can the input string be empty?
# - Can the input string contain spaces?
# - Can the input string contain unicode characters?
# - Can the input string contain all unique/repeating characters?
# - Can the input string contain lowercase and uppercase characters?

# Approach: Sliding Window
# Time complexity: O(n), where n is the length of the input string. We iterate only need to traverse over the string once.
# Space complexity: O(n), where n is the length of the input string. We use a set to store the characters in the current window.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet = set() # Create a set to store the characters in the current window
        left = 0 # Initialize the left pointer at the start of the string
        longest = 0 # Initialize the length of the longest substring

        for right in range(len(s)): # Iterate through the string
            while s[right] in charSet: # If the character at the right pointer is already in the set
                charSet.remove(s[left]) # Remove the character at the left pointer
                left += 1 # Move the left pointer to the right
            charSet.add(s[right]) # Add the character at the right pointer to the set
            longest = max(longest, right - left + 1) # Update the length of the longest substring by comparing it with the length of the current window
        return longest # Return the length of the longest substring
    
# Test cases:
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb")) # Output: 3
print(solution.lengthOfLongestSubstring("bbbbb")) # Output: 1
print(solution.lengthOfLongestSubstring("pwwkew")) # Output: 3
