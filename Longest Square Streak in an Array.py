from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """
        My approach:
        - The problem is to find the longest streak of numbers where each number in the streak is the square of the previous number.
        - We first sort the list to help in easier traversal and checking. By iterating through the sorted numbers, we can attempt to form the longest streak of squares starting from each number.
        - The strategy is to use a set (`num_set`) for fast lookups to check if the square of the current number exists in the list.
        - For each number in the list, we keep multiplying the current number by itself (i.e., squaring it) and check if the result exists in the set.
        - We track the length of the streak and update the `max_streak` whenever a longer streak is found.
        - Finally, if we have found a streak of length 2 or greater, we return the `max_streak`; otherwise, we return -1 (as no valid streak was found).

        Time Complexity: O(n * k), where `n` is the number of elements in `nums` and `k` is the average streak length. Sorting the list takes O(n log n), and checking for the square requires O(k) operations per element.
        Space Complexity: O(n), for storing the set of numbers.

        """
        # Sort the numbers to try to build the streak in ascending order
        nums.sort()
        # Create a set for fast lookup
        num_set = set(nums)
        # Variable to track the longest streak
        max_streak = 0
        
        # Iterate through each number in the sorted list
        for num in nums:
            current = num
            streak_length = 1
            # Keep squaring the current number and checking if it's in the set
            while current * current in num_set:
                current = current * current
                streak_length += 1
            # Update the max streak length
            max_streak = max(max_streak, streak_length)
        
        # If a valid streak of length >= 2 is found, return the length; otherwise, return -1
        return max_streak if max_streak >= 2 else -1
