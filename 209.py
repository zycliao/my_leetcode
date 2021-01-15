from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = n + 1
        for i in range(n):
            sum = 0
            cur_sub_len = 0
            sub_len = n + 1
            for j in range(i, n):
                sum += nums[j]
                cur_sub_len += 1
                if sum >= s:
                    sub_len = cur_sub_len
                    break
            if sub_len < min_len:
                min_len = sub_len
        if min_len > n:
            # no such sub-array exists
            return 0
        else:
            return min_len


class Solution2:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # the inner loop (j) in the first solution doesn't need to start from i
        # Instead, it can start from the last j of the last i
        # This leads to the so-called sliding window method
        n = len(nums)

        if n == 0:
            return 0
        min_len = n + 1
        j = 0
        sum = nums[0]
        # use j as the outer loop might be better
        for i in range(n):
            while 1:
                if sum >= s:
                    if j - i + 1 < min_len:
                        min_len = j - i + 1
                    break
                j += 1
                if j >= n:
                    break
                sum += nums[j]
            sum -= nums[i]

        if min_len > n:
            # no such sub-array exists
            return 0
        else:
            return min_len


class Solution3:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # j as the outer loop
        n = len(nums)

        if n == 0:
            return 0
        min_len = n + 1
        i = 0
        sum = 0
        for j in range(n):
            sum += nums[j]
            while sum >= s:
                length = j - i + 1
                min_len = length if length < min_len else min_len
                sum -= nums[i]
                i += 1
        if min_len > n:
            # no such sub-array exists
            return 0
        else:
            return min_len



if __name__ == '__main__':
    sol = Solution3()
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(sol.minSubArrayLen(s, nums))