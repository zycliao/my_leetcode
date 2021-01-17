class Solution:
    def firstUniqChar(self, s: str) -> str:
        occurance = [0] * 26
        for c in s:
            occurance[ord(c)-ord('a')] += 1
        for c in s:
            if occurance[ord(c)-ord('a')] == 1:
                return c
        return ' '


class Solution2:
    def firstUniqChar(self, s: str) -> str:
        occurance = [50000] * 26
        for i, c in enumerate(s):
            asc = ord(c)-ord('a')
            if occurance[asc] == 50000:
                occurance[asc] = i
            else:
                occurance[asc] = 50001
        m = min(occurance)
        if m < 50000:
            return s[m]
        else:
            return ' '