from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        My approach:
        - The problem asks for the maximum profit that can be achieved by making multiple transactions, 
          where you can buy and sell stocks as many times as you want, but only after selling the previously bought stock.
        - The key observation is that we can sum up all "profitable upward movements" in the price array.
        - For each day, compare the price with the previous day:
            - If today's price is greater than yesterday's, the difference contributes to profit.
            - Accumulate this profit in `res`.
        - This greedy approach ensures that we capture every opportunity to make profit without explicitly tracking buy and sell days.
        
        Time Complexity: O(n) - The list is traversed once.
        Space Complexity: O(1) - No extra space used other than variables.
        """
        res = 0  # Initialize total profit

        # Iterate through the price list, starting from the second day
        for i in range(1, len(prices)):
            # If today's price is greater than yesterday's, add the difference to the profit
            if prices[i - 1] < prices[i]:
                res += prices[i] - prices[i - 1]
        
        return res
