# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return []
        
        result = []
        q = deque()
        q.append(root)
        
        while q:
            size = len(q)
            level = []
            
            for i in range(size):
                node=TreeNode()
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            result.append(sum(level))
            
        max_index = result.index(max(result))
        return max_index+1

   

        
