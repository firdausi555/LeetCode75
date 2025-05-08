class Solution:
    def equalPairs(self, grid):
        dit = defaultdict(int)
        ans=0
        for i in grid:
            dit[str(i)]+=1
        for i in range(len(grid[0])):
            temp=[]
            for j in range(len(grid)):
                temp.append(grid[j][i])
            ans+=dit[str(temp)]
        return ans 
