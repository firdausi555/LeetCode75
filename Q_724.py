class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t=sum(nums)
        l=0
        for i in range(len(nums)):
            #main formula
            r=t-l-nums[i]
            #if its equal then i is the index
            if l==r:
                return i
            
            l+=nums[i]
        return -1
