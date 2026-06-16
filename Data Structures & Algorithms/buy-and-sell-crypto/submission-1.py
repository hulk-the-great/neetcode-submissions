class Solution(object):
    def maxProfit(self, prices):
        left = 0      # buy day
        right = 1     # sell day
        max_profit = 0

        while right < len(prices):
            # profitable trade
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)

            # found cheaper buying day
            else:
                left = right

            right += 1

        return max_profit