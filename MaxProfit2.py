class Solution:
    def maxProfit(self, prices):
        movingMax = 0
        currentMax = 0        
        for i in range(1, len(prices)):
            movingMax = max(movingMax+prices[i]-prices[i-1], prices[i]-prices[i-1])
            print(movingMax)
            print(i)
            currentMax = max(currentMax, movingMax)
            print(currentMax)
        return currentMax

print(Solution().maxProfit([7,1,5,3,6,4]))