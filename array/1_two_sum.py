# 1. Two Sum
# https://leetcode.com/problems/two-sum/

class Solution(object):
    # The twoSum method takes two parameters: a list of numbers (nums) and a target number (target)
    # The method returns a list of two numbers that add up to the target
    def twoSum(self, nums, target):
        # Create an empty dictionary to store the numbers we've seen so far and their indices
        num_map = {}
        # Iterate over the list of numbers with their indices
        for i, num in enumerate(nums):
            # Calculate the number we need to add to the current number to get the target
            complement = target - num
            # If the number we need to add is already in the dictionary
            if complement in num_map:
                # Return the indices of the two numbers that add up to the target
                return [num_map[complement], i]
            # Otherwise, add the current number and its index to the dictionary
            num_map[num] = i
        # If we've iterated over the list and haven't found two numbers that add up to the target, return False
        return False

