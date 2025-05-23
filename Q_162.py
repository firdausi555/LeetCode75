class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=low+((high-low)//2)
            #left neighbour greater
            if mid>0 and nums[mid]<nums[mid-1]:
                high=mid-1
            #right neighbour greater
            elif mid<len(nums)-1 and nums[mid]<nums[mid+1]:
                low=mid+1
            else:
                return mid
