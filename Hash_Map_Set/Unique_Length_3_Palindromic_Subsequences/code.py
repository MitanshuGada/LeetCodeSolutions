class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)

        for m in s:
            right[m]-=1
            for c in left:
                if right[c] > 0:
                    res.add((m, c))
            left.add(m)
        
        return len(res)

"""
Time Complexity: O(N) => iterating over each element. left set will be max 26
Space Complexity: O(N) => since we have a set and a map
"""