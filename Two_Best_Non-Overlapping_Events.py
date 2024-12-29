import heapq
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        """
        My approach:
        - The problem is to find the maximum sum of values from two non-overlapping events.
        - Each event has a start time, an end time, and a value. We need to select two events that don't overlap, and we want to maximize the sum of their values.
        - The approach involves sorting the events based on their start time and using a heap to keep track of events that have ended before the current event starts. This allows us to efficiently check which previous event has the highest value when considering the current event.
        
        Steps:
        1. Sort the events by their start time.
        2. Use a min-heap to store events as tuples `(end_time, value)` and ensure that we can always retrieve the event with the maximum value that ends before the current event starts.
        3. Iterate through the events:
            - For each event, first remove all events from the heap that have ended before the current event starts. Update the `max_value_so_far` to keep track of the highest value encountered so far.
            - Then, update the `max_sum` to consider the sum of the current event's value and the maximum value of the previous non-overlapping events.
        4. The result is the maximum value of `max_sum`, which gives the sum of values from the two non-overlapping events.
        
        Time Complexity: O(n log n), where `n` is the number of events. The events are sorted first, and then each event is pushed and popped from the heap.
        Space Complexity: O(n), for storing the heap.
        """
        
        # Sort events based on start time
        events.sort(key=lambda x: x[0])
        
        # Min-heap to store (end_time, value) of events
        heap = []
        # To store the maximum value encountered so far
        max_value_so_far = 0
        # Variable to store the result (maximum sum of values from two non-overlapping events)
        max_sum = 0
        
        # Iterate through events
        for start, end, value in events:
            # Remove all events from the heap whose end time is less than the current event's start time
            while heap and heap[0][0] < start:
                _, val = heapq.heappop(heap)
                max_value_so_far = max(max_value_so_far, val)
            
            # Update the maximum sum considering the current event and the best previous non-overlapping event
            max_sum = max(max_sum, value + max_value_so_far)
            
            # Push the current event into the heap (by end time)
            heapq.heappush(heap, (end, value))
        
        # Return the maximum sum of two non-overlapping events
        return max_sum
