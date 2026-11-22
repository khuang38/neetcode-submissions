class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        for num in range(len(nums)):
            if (target - nums[num] in dic):
                return [dic[target - nums[num]], num]
            dic[nums[num]] = num
        return []

        