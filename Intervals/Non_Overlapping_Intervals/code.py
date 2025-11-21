class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort based on start times // O(N log(N))
        intervals.sort()
        out = 0
        
        for i in range(1, len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                if intervals[i-1][1] < intervals[i][1]:
                    intervals[i] = intervals[i-1]
                out += 1
        return out

"""
Time Complexity: O(N log(N)) + O(N) // sort and then iterate over each
Space Complexity: O(1) // constant space
"""