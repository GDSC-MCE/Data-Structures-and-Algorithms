class Solution(object):
    def maxProfit(self, prices):
        '''
        Solution 1, we initialize the buy price to first day, find the minimum buy from 2nd day
        subtract the prices[i]-buy to get profit, and check the greater profit.
        '''
        buy= prices[0]
        profit = 0
        
        n = len(prices)
        for i in range(1,n):
            buy = min(buy,prices[i])
            profit = max(prices[i]-buy,profit)
        
        return profit