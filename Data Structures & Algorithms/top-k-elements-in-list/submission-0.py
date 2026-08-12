class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        arr = list(count.keys())

        arr.sort(key=lambda x: count[x], reverse=True)

        return arr[:k]