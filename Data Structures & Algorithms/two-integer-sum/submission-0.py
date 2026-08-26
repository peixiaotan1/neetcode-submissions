class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = dict()

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference not in a:
                a[nums[i]] = i
            else:
                return [a[difference], i]

