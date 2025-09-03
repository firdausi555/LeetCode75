class SmallestInfiniteSet:

    def __init__(self):
        self.temp=1
        self.ans=set()

    def popSmallest(self):
        if self.ans:
            res=min(self.ans)
            self.ans.remove(res) 
            return res
        else:
            self.temp+=1
            return self.temp-1
        

    def addBack(self, num: int):
        if self.temp>num:
            self.ans.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
