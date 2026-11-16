class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        myList = [0]*26
        for i in range(len(s)):
            indexS = ord(s[i]) - ord('a')
            indexT = ord(t[i]) - ord('a')
            myList[indexS] += 1
            myList[indexT] -= 1
        for elem in myList:
            if elem != 0: return False
        return True
        

