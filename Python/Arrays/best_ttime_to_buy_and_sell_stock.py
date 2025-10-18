"""
    Approch : 
        1) consider minPrice as zero index element and maxProfit as 0
        2) traverse throw the array
        3) check if price[i] < minPrice if yes then put minPrice as prices[i]
        4) If not then find the profit as prices[i] - minPrice 
        5) If profit is greater than maxProfit then put it into maxProfit
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice : int = prices[0]
        maxProfit : int = 0 
        for i in range(len(prices)) : 
           if(prices[i] < minPrice) : 
                minPrice = prices[i]
           else : 
                profit : int = prices[i] - minPrice
                maxProfit = profit if profit > maxProfit else maxProfit

        return maxProfit