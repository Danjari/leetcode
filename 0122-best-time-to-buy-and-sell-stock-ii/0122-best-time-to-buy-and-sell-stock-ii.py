class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hi = prices[0]
        lo = prices[0]
        profit = 0
        n = len(prices)
        i = 0
        while i < n-1:
            # where to buy
            while i< n-1 and prices[i]>= prices[i+1]:
                i += 1 
            lo = prices[i]
            
            # where to sell 
            while i< n-1 and prices[i]<= prices[i+1]:
                i += 1 
            hi = prices[i]
            profit += hi - lo

        return profit 
            