from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remaining):
            # Exact amount formed
            if remaining == 0:
                return 0

            # Amount exceeded
            if remaining < 0:
                return float("inf")

            if remaining in memo:
                return memo[remaining]

            minimum_coins = float("inf")

            for coin in coins:
                result = dfs(remaining - coin)

                minimum_coins = min(
                    minimum_coins,
                    1 + result
                )

            memo[remaining] = minimum_coins
            return minimum_coins

        answer = dfs(amount)

        if answer == float("inf"):
            return -1

        return answer