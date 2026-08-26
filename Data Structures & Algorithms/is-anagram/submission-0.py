class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        a = dict()
        b = dict()

        for n in range(len(s)):
            a[s[n]] = a.get(s[n], 0) + 1
        for n in range(len(t)):
            b[t[n]] = b.get(t[n], 0) + 1
        return a == b
