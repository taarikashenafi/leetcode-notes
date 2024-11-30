# 15. 3Sum
# https://leetcode.com/problems/3sum/

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

        nums.sort()  # Sort the array to help with duplicate handling
        results = []  # Initialize results list

        for i in range(len(nums) - 2):  # Iterate through potential first numbers
            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i-1]:  
                continue  

            left, right = i + 1, len(nums) - 1  # Set two-pointer boundaries

            while left < right:  # Two-pointer technique
                current_sum = nums[i] + nums[left] + nums[right]  # Calculate current sum

                if current_sum < 0:  # Sum too small, move left pointer
                    left += 1
                elif current_sum > 0:  # Sum too large, move right pointer
                    right -= 1
                else:  # Found a valid triplet
                    results.append([nums[i], nums[left], nums[right]])  
                    
                    # Skip duplicate left and right values
                    while left < right and nums[left] == nums[left + 1]:  
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  
                        right -= 1
                    
                    left += 1  # Move left pointer
                    right -= 1  # Move right pointer
        
        return results  # Return list of valid triplets