class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter=Counter(arr)
        temp=[]
        for i in counter.values():
            temp.append(i)
        return len(temp)==len(set(temp))

