#Leet Code 70 - EASY

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        My approach:
        - The problem is to determine the number of ways to climb a staircase with 'n' steps,
          where at each step, you can either climb 1 step or 2 steps.
        - If there is only one step (n = 1), the only option is to climb 1 step, so the answer is 1.
        - If there are two steps (n = 2), you can either take two 1-steps or one 2-step, so the answer is 2.
        - For n > 2, I use dynamic programming to build the solution iteratively.
        - I maintain a dp array where dp[i] represents the number of ways to reach the i-th step.
        - I initialize the base cases: dp[0] = 1 and dp[1] = 2.
        - For each step i from 2 to n-1, the number of ways to reach step i is the sum of ways to reach step i-1 and step i-2.
          This is because you can reach step i either from step i-1 (1 step up) or from step i-2 (2 steps up).
        - Finally, I return dp[n-1], which gives the total number of ways to reach the top.

        Time Complexity: O(n) - We iterate through the dp array once, updating each value based on the previous two.
        Space Complexity: O(n) - We store the number of ways for each step in a dp array of size n.
        """
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * n  # Initialize dp array with 0s
        dp[0] = 1  # Base case: 1 way to reach step 0
        dp[1] = 2  # Base case: 2 ways to reach step 1
        
        # Fill the dp array for steps 2 to n-1
        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]  # Total ways to reach step i is the sum of ways to reach i-1 and i-2
        
        return dp[n-1]  # Return the total number of ways to reach the top
