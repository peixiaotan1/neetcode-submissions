class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxpro = 0

        for i in prices[1:]:
            profit = i - minprice
            maxpro = max(profit, maxpro)
            minprice = min(i, minprice)

        return maxpro
