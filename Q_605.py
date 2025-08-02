class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        length = len(flowerbed)
        i = 0
        while i < length and n > 0:
            if flowerbed[i] == 1:
                i += 2 
            elif i == length - 1 or flowerbed[i + 1] == 0:
                n -= 1
                i += 2  
            else:
                i += 3  
        return n == 0  
