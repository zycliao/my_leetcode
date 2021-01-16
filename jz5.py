class Solution:
    def replaceSpace(self, s: str) -> str:
        # return s.replace(' ', '%20')  :)

        s = list(s)
        n = len(s)
        cnt = 0
        for c in s:
            if c == ' ':
                cnt += 1

        s = s + [' ']*(cnt*2)
        r = cnt*2 + n - 1
        for l in range(n-1, -1, -1):
            if l == r:
                break
            if s[l] == ' ':
                r -= 3
                s[r+1: r+4] = '%20'
            else:
                s[r] = s[l]
                r -= 1
        return ''.join(s)


if __name__ == '__main__':
    sol = Solution()
    print(sol.replaceSpace("We are happy."))