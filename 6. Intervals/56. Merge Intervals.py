class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # The goal is to merge overlapping ranges into a single range.
     merged = []
     
     # Step 1: Sort intervals by the start time
     intervals.sort(key=lambda x: x[0])

     for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
     return merged

    # Time: O(nlogn) => Because of the sorting algorithm
    # Space: O(n) => Because of the merged list 