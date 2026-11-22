class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        __ = Counter(nums)
        top_k_keys = [yo for yo, _ in __.most_common(k)]
        return top_k_keys

        