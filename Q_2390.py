class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        [stack.pop() if i == "*" else stack.append(i) for i in s]
        return "".join(stack)
