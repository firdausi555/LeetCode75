# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        def fn(node,level):
            if node==None:
                return

            if len(stack)==level:
                stack.append(node.val)

            fn(node.right,level+1)
            fn(node.left,level+1)
        
        fn(root,0)
        return stack
