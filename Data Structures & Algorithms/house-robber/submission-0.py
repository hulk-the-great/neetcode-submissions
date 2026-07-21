
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # rob1 and rob2 store the previous two results
        for money in nums:
            temp = max(money + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2