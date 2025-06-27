# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxval):
            if not node:
                return 0
            if node.val >=maxval:
                good = 1  
            else: good =0
            maxval = max(maxval, node.val)

            left =dfs(node.left, maxval)
            right = dfs(node.right, maxval)

            return good +left +right

        return dfs(root, root.val)
