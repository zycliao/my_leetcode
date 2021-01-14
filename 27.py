from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 如果发现val，把它和nums里最后一个非val元素交换
        # （逻辑有点太复杂
        i = 0
        cnt = 0
        n = len(nums) - 1
        if len(nums) == 0:
            return 0

        while i < n - cnt:
            # nums[n-cnt]永远不是val
            while nums[n - cnt] == val:
                cnt += 1
                if cnt > n:
                    return 0
            if i >= n - cnt:
                break

            if nums[i] == val:
                nums[i] = nums[n - cnt]
                nums[n - cnt] = val
                cnt += 1
                i += 1
            else:
                i += 1
        if i == n - cnt:
            if nums[i] == val:
                return n - cnt
            else:
                return n + 1 - cnt
        else:
            return n + 1 - cnt

class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 双指针。slow pointer的范围是所有已经确定的非val元素，slow和fast之间的数量是已经确定的val元素的数量
        slow = 0
        fast = 0
        length = len(nums)
        while fast < length:
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        return length - fast + slow



if __name__ == '__main__':
    sol = Solution2()
    nums = [2,4,4,4,0]
    val = 4
    ret = sol.removeElement(nums, val)
    print(ret)
    print(nums)