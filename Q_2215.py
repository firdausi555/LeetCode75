class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        result1=set(nums1)
        result2=set(nums2)
        temp1=[]
        temp2=[]
        answer=[]
        for i in result1:
            if i not in result2:
                temp1.append(i)
                
        for j in result2:
            if j not in result1:
                temp2.append(j)
                
        answer.append(temp1)
        answer.append(temp2)
        return answer
