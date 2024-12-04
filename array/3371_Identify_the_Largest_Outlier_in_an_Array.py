from collections import Counter  # Import Counter for frequency mapping

class Solution(object):
    def getLargestOutlier(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Step 1: Calculate the total sum of the array
        # This will help in identifying the potential outlier.
        total_sum = sum(nums)

        # Step 2: Create a frequency map of the array using Counter
        # This allows for efficient lookups and verification of conditions.
        count = Counter(nums)

        # Step 3: Initialize the variable to track the largest outlier
        # Start with negative infinity to ensure any valid number replaces it.
        max_outlier = float('-inf')

        # Step 4: Iterate through the array to evaluate each number
        for num in nums:
            # Calculate the potential outlier using the formula:
            # `total_sum - num - num` ensures we exclude `num` and validate the remaining sum.
            outlier = total_sum - num - num

            # Validate if the calculated `outlier` exists in the array
            # Condition: count[outlier] > (outlier == num)
            # - If `outlier == num`, ensure it occurs more than once to be valid.
            if count[outlier] > (outlier == num):
                # Update max_outlier with the largest valid outlier found so far
                max_outlier = max(max_outlier, outlier)

        # Step 5: Return the largest valid outlier
        return max_outlier