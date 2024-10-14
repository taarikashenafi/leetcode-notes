# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """        
        n = len(nums)
        # if the array is empty, return an empty array
        if n == 0: return []
        # initialize two pointers, i and j, to the start and end of the array
        i,j = 0,n-1
        # create a result array the same size as the input array to store our answer
        res = [0] * n
        # loop through the array in reverse order, starting from the end
        for k in reversed(range(n)):
            # calculate the squares of the elements at i and j
            i_sqrd = nums[i]**2
            j_sqrd = nums[j]**2
            # if the square of the element at i is greater than the square of the element at j
            if i_sqrd > j_sqrd:
                # add the square of the element at i to the end of the result array
                res[k] = i_sqrd
                # move the pointer i to the right
                i += 1
            else:
                # add the square of the element at j to the end of the result array
                res[k] = j_sqrd
                # move the pointer j to the left
                j -= 1
        # return the result array
        return res
