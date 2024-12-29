from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        My approach:
        - The problem is to find the minimum number of jumps needed to reach the last index of the array `nums`.
        - Each element in `nums` represents the maximum jump length from that position.
        - The approach involves a greedy method:
            1. Iterate through the array while maintaining two key variables:
                - `current_end`: The farthest point reachable with the current number of jumps.
                - `farthest`: The farthest point reachable from the current position.
            2. Increment the jump counter when reaching `current_end`, as this indicates the need for another jump.
            3. Break early if `current_end` reaches or exceeds the last index.

        Time Complexity: O(n), where `n` is the length of `nums`.
        - We iterate through the array once.
        Space Complexity: O(1), as no additional data structures are used.
        """
        n = len(nums)
        if n == 1:
            return 0  # If there's only one element, no jumps are needed.

        jumps = 0  # Count of jumps required.
        current_end = 0  # The farthest point reachable with the current number of jumps.
        farthest = 0  # The farthest point reachable at any point.

        for i in range(n - 1):  # Iterate until the second-to-last index.
            farthest = max(farthest, i + nums[i])  # Update the farthest point reachable.
            if i == current_end:  # If the current index matches the end of the current jump range:
                jumps += 1  # Increment the jump counter.
                current_end = farthest  # Update the end of the current jump range.

                if current_end >= n - 1:  # If we can reach or exceed the last index:
                    break  # Exit the loop.

        return jumps
