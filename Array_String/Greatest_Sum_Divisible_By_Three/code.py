class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        if totalSum % 3 == 0:
            return totalSum
        hMap = {0: 0, 1: 0, 2: 0}

        for i in nums:
            tempMap = hMap.copy()
            for j in range(3):
                rem = (tempMap[j] + i) % 3
                hMap[rem] = max(hMap[rem], tempMap[j] + i)

        return hMap[0]
"""
Time Complexity: O(N) // Iterating over all intervals
Space Complexity: O(1) // Using variables, constant space
"""