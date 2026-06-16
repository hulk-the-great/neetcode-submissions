class Solution(object):
    def maxProfit(self, prices):
        result = 0

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                result = max(result, profit)

        return result