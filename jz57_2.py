import math
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        n = int((-1+math.sqrt(1+8*target))/2)
        if n < 2:
            return []
        res = []
        for m in range(n, 1, -1):
            mid = target // m
            l = mid - m // 2
            r = l + m - 1
            sum = (l+r)*m//2
            if sum == target:
                res.append(list(range(l, r+1)))
            elif sum < target:
                if (target - sum) % m == 0:
                    d = (target - sum) // m
                    res.append(list(range(l+d, r+d+1)))
            else:
                raise ValueError
        return res


class Solution2:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        n = int((-1+math.sqrt(1+8*target))/2)
        if n < 2:
            return []
        res = []
        for m in range(n, 1, -1):
            nu = 2 * target - m*(m-1)
            de = 2 * m
            if not nu % de:
                start = nu // de
                res.append([k for k in range(start, start+m)])
        return res




if __name__ == '__main__':
    sol = Solution2()
    for i in range(9, 20):
        print(sol.findContinuousSequence(i))