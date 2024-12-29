from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        My approach:
        - The goal is to find the contiguous subarray with the largest sum.
        - This problem is effectively solved using Kadane's Algorithm:
            1. Initialize two variables:
                - `currentsum`: Tracks the running sum of the current subarray.
                - `sum`: Stores the maximum sum encountered so far.
            2. Iterate through the array:
                - If `currentsum` becomes negative, reset it to the current element (`i`) since a negative running sum cannot contribute to a larger maximum.
                - Otherwise, add the current element to `currentsum`.
                - Update `sum` if `currentsum` exceeds the previous maximum.
            3. At the end of the loop, `sum` holds the largest subarray sum.

        Time Complexity: O(n), where `n` is the length of `nums`.
        - The array is traversed once.
        Space Complexity: O(1), as no additional data structures are used.
        """
        sum = nums[0]  # Initialize the maximum sum with the first element.
        currentsum = nums[0]  # Initialize the running sum with the first element.

        for i in nums[1:]:  # Iterate through the array starting from the second element.
            if currentsum < 0:  
                currentsum = i  # Reset `currentsum` if it's negative.
            else:
                currentsum += i  # Add the current element to the running sum.
            
            if currentsum > sum:  
                sum = currentsum  # Update the maximum sum if the current sum is greater.

        return sum
