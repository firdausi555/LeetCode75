class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        p1 = 0
        p2 = len(nums) - 1
        count = 0
        
        while p1 < p2:
            current_sum = nums[p1] + nums[p2]
            if current_sum == k:
                count += 1
                p1 += 1
                p2 -= 1
            elif current_sum < k:
                p1 += 1
            else:
                p2 -= 1
                
        return count
