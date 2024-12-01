# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"  

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Can the array be empty?
        # Are duplicate triplets allowed?
        # What is the maximum array length?
        # How to handle zero as a potential sum?

        # Two-pointer approach after sorting
        # Avoid duplicates by skipping repeated values
        # Time complexity O(N²), space complexity O(1) excluding output

        # Sort the array to help with duplicate handling
        nums.sort()  

        # Initialize results list
        results = []  

        # Iterate through potential first numbers
        for i in range(len(nums) - 2):  
            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i-1]:  
                continue  

            # Set two-pointer boundaries
            left, right = i + 1, len(nums) - 1  

            # Two-pointer technique
            while left < right:  
                # Calculate current sum
                current_sum = nums[i] + nums[left] + nums[right]  

                # Sum too small, move left pointer
                if current_sum < 0:  
                    left += 1
                # Sum too large, move right pointer
                elif current_sum > 0:  
                    right -= 1
                # Found a valid triplet
                else:  
                    # Add triplet to results list
                    results.append([nums[i], nums[left], nums[right]])  

                    # Skip duplicate left and right values
                    while left < right and nums[left] == nums[left + 1]:  
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  
                        right -= 1

                    # Move left and right pointers
                    left += 1  
                    right -= 1
        
        # Return list of valid triplets
        return results  