# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Clarifiying Questions:
# - Can the input list be empty?
# - Are duplicate prices allowed?
# - What is the maximum array length?
# - How to handle negative prices?

# Approach: Two Pointers
# Time complexity: O(N), where N is the length of the input list.
# Space complexity: O(1), since we are not using any additional data structures

class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0] # Initialize the buy price as the first price in the list
        max_profit = 0 # Initialize the maximum profit as 0
        for sell in prices: # Iterate through the list of prices
            buy = min(buy, sell) # Update the buy price to the minimum of the current buy price and the current sell price
            curr_profit = sell - buy # Calculate the current profit as the difference between the current sell price and the buy price
            max_profit = max(max_profit, curr_profit) # Update the maximum profit as the maximum of the current profit and the maximum profit so far
        return max_profit # Return the maximum profit
    
# Test cases:
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4])) # Output: 5
print(solution.maxProfit([7,6,4,3,1])) # Output: 0
print(solution.maxProfit([2,4,1])) # Output: 2
