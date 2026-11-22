class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        l = list()
        top_k_keys = [key for key, count in cnt.most_common(k)]
        return top_k_keys

        