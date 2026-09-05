class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        lmax, rmax = 0, 0
        res = 0
        while l < r:
            
            if height[l] < height[r]:
                lmax = max(height[l], lmax)
                res += lmax - height[l]
                l += 1
            else:
                rmax = max(height[r], rmax)
                res += rmax - height[r]
                r -= 1
        return res