class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        out = []
        for i in range(len(candies)):
            temp = candies[i] + extraCandies
            if temp >= max(candies):
                out.append(True)
            else:
                out.append(False)
                
        return out
