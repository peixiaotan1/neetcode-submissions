class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxpro = 0

        for price in prices[1:]:
            minprice = min(minprice, price)
            maxpro = max(maxpro, price-minprice)
        return maxpro