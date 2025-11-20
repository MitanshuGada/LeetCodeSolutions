class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1 <= nums.length <= 100
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = {-2: 0, -1: 0}

        for i in range(n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n-1]
        
        """
        Space Complexity: O(N) => saving N numbers in the Hash Map
        Time Complexity: O(N) => iterating over each value once in the array
        """