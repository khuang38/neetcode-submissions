class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0]*26
        for idx in range(len(s)):
            charS, charT = s[idx], t[idx]
            count[ord(charS) - ord('a')] += 1
            count[ord(charT) - ord('a')] -= 1
        for c in count:
            if c != 0:
                return False
        return True

        