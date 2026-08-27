class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()

        for n in range(len(nums)):
            diff = target - nums[n]
            if diff not in a:
                a[nums[n]] = n
            else:
                return [a[diff], n]