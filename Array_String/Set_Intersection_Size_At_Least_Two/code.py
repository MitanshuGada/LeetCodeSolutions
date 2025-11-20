class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 2

        intervals.sort(key = lambda x : (x[1], -x[0]))
        res = 0
        p1, p2 = -1, -1

        for left, right in intervals:
            if p2 < left:
                res += 2
                p1, p2 = right - 1, right
            elif p1 < left:
                res += 1
                if p2 == right:
                    p1 = right - 1
                else:
                    p1, p2 = p2, right
            
        return res
"""
Time Complexity: O(Nlog(N)) + O(N) // Sorting and iterating over all intervals
Space Complexity: O(1) // Using variables, constant space
"""