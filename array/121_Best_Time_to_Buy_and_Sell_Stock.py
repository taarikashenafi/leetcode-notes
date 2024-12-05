# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Approach: One-Pass Solution using Two Pointers (buy and sell)
# 
# The goal is to find the maximum profit from a list of stock prices where the index
# represents the day. We aim to determine the optimal days to buy and sell.
#
# In this approach, we maintain two variables:
# - `buy`: Tracks the lowest price seen so far, representing the best day to buy.
# - `max_profit`: Tracks the maximum profit that can be achieved based on the current `sell` price.
#
# As we iterate through the list of prices:
# 1. Update `buy` with the minimum of the current `buy` and the current price (`sell`).
# 2. Calculate the potential profit by subtracting `buy` from the current price (`sell`).
# 3. Update `max_profit` with the maximum of the current `max_profit` and the potential profit.
#
# The algorithm efficiently finds the maximum profit by scanning the prices once,
# making it both time and space efficient.

# Clarifiying Questions:
# - Can the input list be empty?
# - Are duplicate prices allowed?
# - What is the maximum array length?
# - How to handle negative prices?

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        max_profit = 0
        for sell in prices:
            buy = min(buy, sell)
            curr_profit = sell - buy
            max_profit = max(max_profit, curr_profit)
        return max_profit
    
# Time complexity: O(N)
# Space complexity: O(1)

# Example:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.   

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we return 0.

