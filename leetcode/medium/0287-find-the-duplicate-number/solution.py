class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        seen = nums[0]
        for num in range(1, len(nums)):
            if nums[num] == seen:
                return nums[num]
            seen = (max(seen, nums[num]) - min(seen, nums[num])) + 1