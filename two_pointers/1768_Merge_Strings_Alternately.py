# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/

# CLarifying Questions:
# - Can the input strings be empty?
# - Are duplicate characters allowed?
# - What is the maximum string length?
# - How to handle strings of different lengths?

# Approach: Two Pointers
# Time complexity: O(n), where n is the length of the longest string.
# Space complexity: O(n), where n is the length of the longest string.


# To solve this problem, we use two pointers to traverse both strings simultaneously.
# We maintain a list, `ans`, to store the characters of the strings in alternating order.
# We then traverse the strings using a while loop, adding a character from the first string to `ans` if we're within its length, and adding a character from the second string if we're within its length.
# Finally, we return the joined characters of `ans` as the result string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        len1, len2 = len(word1), len(word2) # Get the length of both strings
        ans = [] # Initialize an empty list to store the result
        i = 0 # Initialize a counter to loop through the strings
        
        while i < len1 or i < len2: # Loop until we've traversed the entire string
            if i < len1: # If we haven't reached the end of the first string, append the character at the current index to `ans`
                ans.append(word1[i])
            
            if i < len2: # If we haven't reached the end of the second string, append the character at the current index to `ans`
                ans.append(word2[i])
            
            i += 1 # Increment the counter
        
        return ''.join(ans) # Return the joined characters of `ans` as the result string
    

# Test cases:
solution = Solution()
print(solution.mergeAlternately("abc", "pqr")) # Output: "apbqcr"
print(solution.mergeAlternately("ab", "pqrs")) # Output: "apbqrs"
print(solution.mergeAlternately("abcd", "pq")) # Output: "apbqcd"