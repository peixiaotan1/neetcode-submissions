class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0

        for x in nums:
            if x-1 in nums:
                continue
            length = 1
            while x+length in nums:
                length += 1
            
            best = max(length, best)
        return best