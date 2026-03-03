class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(list)
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 0
        sorted_res = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
        ans = list(sorted_res)
        return ans[:k]
        