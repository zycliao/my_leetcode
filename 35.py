from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if target <= n:
                return i
        return len(nums)

class Solution2:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 二分
        start = 0
        end = len(nums) - 1
        # target有可能不在start-end之间
        while end - start > 1:
            mid = (start+end)//2
            if target < nums[mid]:
                end = mid - 1
            elif target == nums[mid]:
                return mid
            else:
                start = mid + 1
        if target <= nums[start]:
            return start
        elif target <= nums[end]:
            return end
        else:
            return end + 1