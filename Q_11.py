class Solution:
    def maxArea(self, height):
        maxA=0
        left=0
        right=len(height)-1
        while left<=right:
            maxA=max(maxA,(right-left)*min(height[left],height[right]))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxA
