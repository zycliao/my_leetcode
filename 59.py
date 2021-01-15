from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0]*n for k in range(n)]
        flag = 0
        i, j = 0, -1
        for x in range(1, n*n+1):
            if flag == 0:
                j += 1
                if j+1>=n or mat[i][j+1] != 0:
                    flag = 1
            elif flag == 1:
                i += 1
                if i+1>=n or mat[i+1][j] != 0:
                    flag = 2
            elif flag == 2:
                j -= 1
                if j==0 or mat[i][j-1] != 0:
                    flag = 3
            else:
                i -= 1
                if i == 0 or mat[i-1][j] != 0:
                    flag = 0
            mat[i][j] = x
        return mat


class Solution2:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # no judging. determine the length in advance
        mat = [[0]*n for k in range(n)]
        i, j = 0, -1
        a = n
        x = 0
        while a > 0:
            for _ in range(a):
                j += 1
                x += 1
                mat[i][j] = x
            a -= 1
            for _ in range(a):
                i += 1
                x += 1
                mat[i][j] = x
            for _ in range(a):
                j -= 1
                x += 1
                mat[i][j] = x
            a -= 1
            for _ in range(a):
                i -= 1
                x += 1
                mat[i][j] = x

        return mat


if __name__ == '__main__':
    sol = Solution2()
    print(sol.generateMatrix(5))