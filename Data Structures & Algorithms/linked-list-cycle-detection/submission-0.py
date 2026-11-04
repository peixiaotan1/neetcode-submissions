# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        curn = head
        while curn and curn.next:
            cur = cur.next
            curn = curn.next.next
            if cur == curn:
                return True
        return False