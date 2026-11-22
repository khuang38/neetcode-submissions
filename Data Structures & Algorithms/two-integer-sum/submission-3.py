class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        res = [0]*2
        for num in range(len(nums)):
            if (target - nums[num] in dic):
                res[0] = dic[target - nums[num]]
                res[1] = num
                break
            dic[nums[num]] = num
        return res

        