from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        My approach:
        - The problem asks to find the minimum cost to climb to the top of a staircase.
        - You can start from either the 0th or the 1st step, and from each step, you can climb one or two steps forward.
        - The key is to find the minimum cost to reach each step and use memoization to avoid redundant calculations.
        - I use a recursive function `mincost(i)` to compute the minimum cost to reach the i-th step.
        - Base cases: The cost to reach the 0th and 1st steps is 0 (since we start from those steps).
        - For any other step i:
            - I calculate the cost to reach it as the minimum of:
              1. The cost to reach (i-2) + cost[i-2] (if stepping two steps),
              2. The cost to reach (i-1) + cost[i-1] (if stepping one step).
        - Memoization stores the result for each step to avoid recomputation.
        - The result is the minimum cost to reach either the (n-2)th step or the (n-1)th step.
        
        Time Complexity: O(n) - Each step is computed once and stored in the memo dictionary.
        Space Complexity: O(n) - The space used by the memo dictionary and recursion stack.
        """
        memo = {0: 0, 1: 0}  # Initialize memoization with base cases

        def mincost(i):
            # Check if already computed
            if i in memo:
                return memo[i]
            # Compute and store the minimum cost for step i
            memo[i] = min(mincost(i-2) + cost[i-2], mincost(i-1) + cost[i-1])
            return memo[i]

        # Compute the minimum cost to reach the top
        return mincost(len(cost))
