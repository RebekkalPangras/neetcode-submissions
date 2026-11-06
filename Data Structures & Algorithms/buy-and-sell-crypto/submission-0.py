class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        print("Prices: ", prices)
        print("min_price: ", min_price, "max_profit: ", max_profit)
        for i in range(1, len(prices)):
            print("Current Price: ", prices[i])
            if prices[i]<min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            print("min_price: ", min_price, "max_profit: ", max_profit)
        return max_profit