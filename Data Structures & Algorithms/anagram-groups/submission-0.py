class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            myset = [0]*26
            for char in string:
                myset[ord(char) - ord('a')] += 1
            groups[tuple(myset)].append(string)
        return list(groups.values())

        