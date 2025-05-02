class Solution:
    def productExceptSelf(self, nums):
        leftArr = [1] * len(nums)
        rightArr = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            leftArr[i] *= left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            rightArr[i] *= right
            right *= nums[i]

        return [leftArr[i] * rightArr[i] for i in range(len(nums))]
