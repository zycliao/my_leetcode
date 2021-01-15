from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        ref = [-1]*len(nums)
        for x in nums:
            if ref[x] == -1:
                ref[x] = x
            else:
                return x


class Solution2:
    def findRepeatNumber(self, nums: List[int]) -> int:
        # no extra array. space complexity O(1)
        for i, x in enumerate(nums):
            if x == i:
                continue
            s = nums[x]
            if s == x:
                return s
            nums[x], nums[i] = x, s


if __name__ == '__main__':
    sol = Solution2()
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(sol.findRepeatNumber(nums))