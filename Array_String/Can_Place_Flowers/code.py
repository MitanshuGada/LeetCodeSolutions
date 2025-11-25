class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)
        i = 0
        while i < N:
            if flowerbed[i] == 0:
                prev = flowerbed[i-1] if i > 0 else 0
                nxt = flowerbed[i+1] if i < N-1 else 0
                if prev == flowerbed[i] and nxt == flowerbed[i]:
                    n-=1
                    i+=2
                else:
                    i += 1
            else:
                i += 2
        
        return n <= 0

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""