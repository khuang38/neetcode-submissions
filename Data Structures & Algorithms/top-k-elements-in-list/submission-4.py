class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        heap = []
        for key, val in dic.items():
            heapq.heappush_max(heap, (val, key))
        res = []
        for i in range(k):
            res.append(heapq.heappop_max(heap)[1])
        return res
