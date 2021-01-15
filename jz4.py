from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        if h == 0:
            return False
        w = len(matrix[0])
        if w == 0:
            return False
        max_i = h - 1
        if target < matrix[0][0]:
            return False
        for j in range(w):
            aa, bb = 0, max_i
            if target > matrix[bb][j]:
                continue
            while bb - aa > 1:
                m = (aa + bb) // 2
                if matrix[m][j] == target:
                    return True
                elif matrix[m][j] < target:
                    aa = m
                else:
                    bb = m
            if bb - aa <= 1:
                if matrix[aa][j] == target or matrix[bb][j] == target:
                    return True
            max_i = bb - 1
        return False

class Solution2:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        if h == 0:
            return False
        w = len(matrix[0])
        if w == 0:
            return False
        i = 0
        j = w - 1
        while i < h and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


if __name__ == '__main__':
    sol = Solution2()
    m =  [[3,5,9,9,14],[7,8,11,15,15],[8,10,16,16,17]]
    print(sol.findNumberIn2DArray(m, 12))