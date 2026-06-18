class Solution(object):
    def minCostClimbingStairs(self, cost):
        if len(cost) <= 2:
            return min(cost)
        
        prev1, prev2 = cost[1], cost[0]

        for i in range(2, len(cost)):
            curr = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = curr

        return min(prev1, prev2)
    