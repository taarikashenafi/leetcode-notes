# 896. Monotonic Array
# https://leetcode.com/problems/monotonic-array/

class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # get the length of the array
        n = len(nums)
        # if the array is empty, return True
        if n == 0: return True
        # get the first and last elements of the array
        first,last = nums[0],nums[n-1]
        # if the first element is greater than the last element, then the array is monotonically decreasing
        if first > last:
            # loop through the array from the second element to the second to last element
            for k in range(n-1):
                # if the current element is less than the next element, then the array is NOT monotonically decreasing
                if nums[k] < nums[k+1]: 
                    # return False
                    return False
        # if the first element is equal to the last element, then the array is monotonically constant
        elif first == last:
            # loop through the array from the second element to the second to last element
            for k in range(n-1):
                # if the current element is NOT equal to the next element, then the array is NOT monotonically constant
                if nums[k] != nums[k+1]: 
                    # return False
                    return False
        # if the first element is less than the last element, then the array is monotonically increasing
        else:
            # loop through the array from the second element to the second to last element
            for k in range(n-1):
                # if the current element is greater than the next element, then the array is NOT monotonically increasing
                if nums[k] > nums[k+1]: 
                    # return False
                    return False
        # if the array is monotonically decreasing, constant, or increasing, then return True
        return True
