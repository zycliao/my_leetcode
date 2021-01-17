from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        if r <= 1:
            return []
        while 1:
            if l == r:
                break
            s = nums[l] + nums[r]
            if s == target:
                return [nums[l], nums[r]]
            elif s > target:
                r -= 1
            else:
                l += 1
        return []