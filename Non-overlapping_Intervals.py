import heapq
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        My approach:
        - The task is to remove the minimum number of intervals to ensure no two intervals overlap.
        - Steps:
          1. Sort the intervals based on their start times.
          2. Use a min-heap to keep track of the end times of non-overlapping intervals.
          3. Iterate through the sorted intervals:
             - If the smallest end time in the heap (top of the heap) is less than or equal to the start time of the current interval, 
               pop the heap as it indicates no overlap with the current interval.
             - Push the current interval's end time into the heap.
          4. The heap contains the end times of the maximum number of non-overlapping intervals.
          5. To calculate the intervals to remove, subtract the size of the heap (non-overlapping intervals) from the total number of intervals.
        
        Time Complexity: O(n log n), where `n` is the number of intervals.
        - Sorting the intervals takes O(n log n), and heap operations take O(log n) for each interval.
        Space Complexity: O(n), for the min-heap storage.
        """

        # Min-heap to store end times of intervals
        minheap = []

        # Sort intervals based on their start times
        intervals.sort()

        # Iterate through the sorted intervals
        for i in intervals:
            start, end = i
            # If the smallest end time in the heap is less than or equal to the current start time,
            # remove it from the heap (indicating no overlap)
            if minheap and minheap[0] <= start:
                heapq.heappop(minheap)
            # Add the current interval's end time to the heap
            heapq.heappush(minheap, end)

        # Calculate the number of intervals to remove
        count = len(intervals) - len(minheap)
        return count
