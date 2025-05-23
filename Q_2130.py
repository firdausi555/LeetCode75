# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=head
        slow=head
        stack=[]
        while fast and fast.next:
            stack.append(slow.val)
            slow=slow.next
            fast=fast.next.next
        maxSum=0
        while slow:
            maxSum=max(maxSum,slow.val+stack.pop())
            slow=slow.next
        return maxSum
