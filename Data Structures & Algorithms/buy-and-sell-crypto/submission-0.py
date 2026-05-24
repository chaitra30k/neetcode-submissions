class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=float('inf')
        sell=float('-inf')
        for x in prices:
            buy=min(x,buy)
            sell=max(sell,x-buy)
        return sell