# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # `left` is the starting index of our sliding window
        left = 0
        # `seen` is a dictionary that maps characters to their most recent index
        seen = {}
        # `longest` is the longest substring found so far
        longest = 0
        # Iterate over the characters in the string, `right` is the current index
        for right, curr in enumerate(s):
            # If the current character is already in `seen`, that means we've seen it before
            # So we need to move the `left` pointer to the right of the previous occurrence
            if curr in seen:
                # The `max` is used to make sure `left` is at least one to the right of the previous occurrence
                left = max(left, seen[curr] + 1)
            # Update the `longest` if the current substring is longer
            longest = max(longest, right - left + 1)
            # Update the `seen` dictionary with the current character and its index
            seen[curr] = right
        # Return the longest substring found
        return longest


        