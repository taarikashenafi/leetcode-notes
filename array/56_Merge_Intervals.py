# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

# Clarification:
# - Can the input intervals be empty?
# - Are duplicate intervals allowed?
# - What is the maximum number of intervals?
# - Are all intervals of the same length?

# Approach: Sorting
# Time complexity: O(n log n), where n is the number of intervals. Built in sorting function is always O(n log n).
# Space complexity: O(n), where n is the number of intervals. We are creating a new list that is only as large the input list itself.

class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0]) # Sort the intervals by the start time
        merged = [] # Initialize a list to store the merged intervals

        for interval in intervals: # Iterate over each interval
            if not merged or merged[-1][1] < interval[0]: # If the merged list is empty or the current interval does not overlap with the previous interval
                merged.append(interval) # Add the current interval to merged 
            else:
                merged[-1][1] = max(merged[-1][1], interval[1]) # Otherwise, merge the current interval with the previous interval
        return merged # Return the merged intervals

# Test cases:
solution = Solution()
print(solution.merge([[1,3],[2,6],[8,10],[15,18]])) # Output: [[1,6],[8,10],[15,18]]
print(solution.merge([[1,4],[4,5]])) # Output: [[1,5]]
print(solution.merge([[1,4],[0,4]])) # Output: [[0,4]]