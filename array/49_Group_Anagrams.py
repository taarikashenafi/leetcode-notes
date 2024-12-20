# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

# Clarification:
# - Can the input strings be empty?
# - Are duplicate strings allowed?
# - What is the maximum string length?
# - How to handle strings of different lengths?

# Approach: Sorting
# Time complexity: O(NK log K), where N is the number of strings and K is the maximum length of a string.
# Space complexity: O(NK), where N is the number of strings and K is the maximum length of a string.

# Intuition: Two strings are anagrams if and only if their character counts are the same.
# Algorithm: We use a hashmap to store the character counts of each string as the key,
# and append the strings with the same counts to the corresponding value in the hashmap.


from collections import defaultdict # Import the defaultdict class from the collections module

class Solution(object):
    def groupAnagrams(self, strs):
        ans = defaultdict(list) # Create a defaultdict to store the anagrams
        for word in strs: # Iterate through the list of strings
            ans[str(sorted(word))].append(word) # Sort the characters in the string and append the string to the corresponding key in the defaultdict
        return ans.values() # Return the values of the defaultdict
    
# Test cases:
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(solution.groupAnagrams([""])) # Output: [[""]]
print(solution.groupAnagrams(["a"])) # Output: [["a"]]