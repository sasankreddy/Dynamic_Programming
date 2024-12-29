from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        My approach:
        - The task is to find the maximum product of a contiguous subarray.
        - The presence of negative numbers and zeros complicates the problem since:
            - A single negative number can flip the sign of the product.
            - Zeros break the continuity of the subarray product.
        - To address this:
            1. Traverse the array twice:
                - Forward traversal:
                    - Maintain a `current` running product.
                    - Reset `current` to 1 if it becomes zero.
                    - Track the maximum product (`maxprod`) during the traversal.
                - Backward traversal:
                    - Reverse the array and perform a similar traversal to handle cases where the maximum product subarray lies towards the end of the array.
            2. Compare the results of the forward and backward traversals and return the larger value.
        - This approach ensures that all cases, including negative numbers and zeros, are handled efficiently.

        Time Complexity: O(n), where `n` is the length of the array.
        - Each element is traversed twice.
        Space Complexity: O(1), as no additional data structures are used.
        """
        if len(nums) == 1:
            return nums[0]  # Single-element case.

        maxprod = float('-inf')  # Initialize the maximum product.
        current = 1  # Running product for the forward pass.

        # Forward traversal
        for i in range(len(nums)):
            current *= nums[i]  # Update running product.
            if current > maxprod:
                maxprod = current  # Update maximum product.
            if current == 0:  # Reset if zero is encountered.
                current = 1

        nums1 = nums[::-1]  # Reverse the array for backward traversal.
        maxprod1 = float('-inf')  # Initialize for backward pass.
        current1 = 1  # Running product for the backward pass.

        # Backward traversal
        for i in range(len(nums1)):
            current1 *= nums1[i]  # Update running product.
            if current1 > maxprod1:
                maxprod1 = current1  # Update maximum product.
            if current1 == 0:  # Reset if zero is encountered.
                current1 = 1

        # Return the larger of the two maximum products.
        return max(maxprod, maxprod1)
