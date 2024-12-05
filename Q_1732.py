class Solution:
    def largestAltitude(self, gain):
        
        altitudes=[0]
        temp=0
        for i in range(len(gain)):
            temp+=gain[i]
            
            altitudes.append(temp)
        return max(altitudes)
