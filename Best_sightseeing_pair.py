from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        My approach:
        - The goal is to find two indices `i` and `j` (where i < j) that maximize the score:  
          `values[i] + values[j] + i - j`.
        - Steps:
          1. Initialize `max_score` to 0, which will store the maximum score found so far.
          2. Initialize `max_i` to `values[0]`, which will store the maximum value of `values[i] + i` as we iterate through the list.
          3. Loop through the list starting from index 1, for each value `values[j]`:
             - Calculate the score for the current pair `(i, j)` as `max_i + values[j] - j` and update `max_score` if it's greater than the current `max_score`.
             - Update `max_i` to be the maximum of the current `max_i` and the value `values[j] + j` to ensure we always have the best possible value for the next iterations.
          4. Finally, return the maximum score found.
        
        Time Complexity: O(n), where `n` is the length of the `values` list. We only loop through the list once.
        Space Complexity: O(1), as we are using only a constant amount of extra space.
        """
        
        max_score = 0  # To keep track of the maximum score
        max_i = values[0]  # To keep track of the best possible values[i] + i for the given pair
        
        for j in range(1, len(values)):
            # Update the max score for the current pair (i, j)
            max_score = max(max_score, max_i + values[j] - j)
            
            # Update the value of max_i for the next iteration
            max_i = max(max_i, values[j] + j)
        
        return max_score
