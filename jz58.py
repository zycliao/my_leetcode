class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')[::-1]
        s = [c.strip() for c in s if c]
        return ' '.join(s)


class Solution2:
    def reverseWords(self, s: str) -> str:
        s = [c for c in s]
        length = len(s)
        if length == 0:
            return ''
        res = [' '] * length
        r = length - 1

        cnt = 0
        while 1:
            while s[r] == ' ':
                r -= 1
                if r < 0:
                    if cnt != 0:
                        cnt -= 1
                    return ''.join(res[:cnt])
            l = r
            while s[l] != ' ' and l >= 0:
                l -= 1
            l += 1

            for i in range(l, r+1):
                res[cnt] = s[i]
                cnt += 1
            cnt += 1

            if l == 0:
                return ''.join(res[:cnt-1])
            else:
                r = l - 1


if __name__ == '__main__':
    sol = Solution2()
    print(sol.reverseWords("the sky is blue"))


