class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [None, None]
        map = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in map:
                return [map[complement], i]
            map[val] = i
        return [None, None]

        