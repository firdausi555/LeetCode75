class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)

        def helper(m):
            hours=0
            for i in piles :
                hours+=math.ceil(i/m)
            return hours<=h

        while l<r:
            m=(l+r)//2
            if helper(m):
                r=m
            else:
                l=m+1
        return l
