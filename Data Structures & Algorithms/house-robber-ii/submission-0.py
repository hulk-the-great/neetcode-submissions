from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(
            self.helper(nums[1:]),
            self.helper(nums[:-1])
        )

    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for money in nums:
            new_rob = max(rob1 + money, rob2)
            rob1 = rob2
            rob2 = new_rob

        return rob2