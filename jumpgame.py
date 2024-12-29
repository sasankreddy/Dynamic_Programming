from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        My approach:
        - The problem is to determine if it's possible to reach the last index of an array, starting from the first index, 
          by jumping based on the values in the array.
        - Each element `nums[i]` represents the maximum number of indices you can jump forward from index `i`.
        - To solve this problem, we can use a greedy approach:
            - We initialize `farthest` as 0, which represents the farthest index we can reach at any point.
            - We iterate through the array. For each index `i`, we update the farthest index we can reach (`farthest = max(farthest, i + nums[i])`).
            - If at any point, `i` is equal to or greater than `farthest`, it means we can't jump further, and we return `False`.
            - If we can reach or surpass the last index (`farthest >= len(nums) - 1`), we return `True` because it means it's possible to reach the last index.
        - Edge cases:
            - If the first element is `0` and the array has more than one element, it's not possible to make any jumps, so return `False`.
            - If the array has only one element, return `True` because we're already at the last index.
        
        Time Complexity: O(n), where `n` is the length of the array. We only iterate through the array once.
        Space Complexity: O(1), since we only use a few variables to track the farthest index.

        """
        # Edge case: If there's only one element, we can always reach the end
        if len(nums) == 1:
            return True
        
        # If the first element is 0, we can't make any jump
        if nums[0] == 0:
            return False
        
        farthest = 0
        for i in range(len(nums) - 1):
            # Update the farthest index we can reach
            farthest = max(farthest, i + nums[i])
            
            # If we're stuck at this index and can't move further, return False
            if nums[i] == 0 and farthest <= i:
                return False
            
            # If we can reach or surpass the last index, return True
            if farthest >= len(nums) - 1:
                return True
        
        return False
