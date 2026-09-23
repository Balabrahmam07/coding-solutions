class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diff = {}
        for i, num in enumerate(nums):
            n = target - num
            if n in diff:
                return [diff[n], i]
            diff[num] = i
            