from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        My approach:
        - The problem asks to find the maximum profit that can be achieved by buying and selling a stock, where the stock must be bought before it is sold.
        - The goal is to identify the lowest price up to the current day (minimum so far) and calculate the potential profit by selling on the current day.
        - I maintain two variables:
            1. `mini`: Tracks the lowest price seen so far.
            2. `profit`: Tracks the maximum profit calculated so far.
        - For each day's price in the `prices` list:
            - If the current price is less than `mini`, update `mini` to the current price.
            - Otherwise, calculate the profit as the difference between the current price and `mini`. If this profit is greater than the current maximum profit, update `profit`.
        - At the end of the loop, `profit` contains the maximum possible profit.

        Time Complexity: O(n) - The list is traversed once.
        Space Complexity: O(1) - Only two variables (`mini` and `profit`) are used.
        """
        mini = prices[0]  # Initialize to the first day's price
        profit = 0  # Initialize maximum profit to 0

        # Iterate over the prices to calculate maximum profit
        for i in range(len(prices)):
            # Update minimum price if a lower price is found
            if prices[i] < mini:
                mini = prices[i]
            # Update maximum profit if a higher profit is found
            if prices[i] - mini > profit:
                profit = prices[i] - mini
        
        return profit
