class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        res = []
        for num in range(len(nums)):
            if (target - nums[num] in dic):
                res = [dic[target - nums[num]], num]
                break
            dic[nums[num]] = num
        return res

        