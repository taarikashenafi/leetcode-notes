# 704. Binary Search
# https://leetcode.com/problems/binary-search/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # get the length of the input array
        n = len(nums)
        # initialize two pointers, l and r, to the start and end of the array
        l, r = 0, n-1
        # calculate the middle index of the array
        m = (l + r) // 2
        # loop until the pointers cross
        while l <= r:
            # if the target is greater than the element at the middle index
            if target > nums[m]:
                # move the left pointer to the right of the middle index
                l = m + 1
            # if the target is less than the element at the middle index
            if target < nums[m]:
                # move the right pointer to the left of the middle index
                r = m - 1
            # calculate the middle index for the next iteration
            m = (l + r) // 2
            # if the target is equal to the element at the middle index
            if nums[m] == target:
                # return the index
                return m
        # if the target is not found, return -1
        return -1
