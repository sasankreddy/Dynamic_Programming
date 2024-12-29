from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        My approach:
        - The task is to find the length of the longest increasing subsequence (LIS) in the given list `nums`.
        - We use a dynamic programming approach where:
            1. Create a DP array `dp` of size `len(nums)` initialized with `1`.
               - Each element `dp[i]` represents the length of the LIS ending at index `i`.
            2. For each element at index `i`, compare it with all previous elements at index `j` (where `j < i`).
               - If `nums[i] > nums[j]`, it means we can extend the LIS ending at `j` to include `nums[i]`.
               - Update `dp[i]` as `dp[i] = max(dp[i], dp[j] + 1)`.
            3. After processing all indices, the result is the maximum value in the `dp` array.

        Time Complexity: O(n^2), where `n` is the length of the input array.
        - For each element, we compare it with all previous elements.
        Space Complexity: O(n), for the `dp` array used to store LIS lengths.
        """

        # Initialize the DP array where each element is initially 1.
        dp = [1] * len(nums)

        # Iterate through the array to compute LIS lengths.
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:  # Can extend the LIS ending at index j.
                    dp[i] = max(dp[i], dp[j] + 1)

        # Return the maximum length of LIS from the DP array.
        return max(dp)
