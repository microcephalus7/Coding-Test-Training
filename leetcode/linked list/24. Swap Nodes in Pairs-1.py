# 모든 두 쌍의 노드 교환

# 값만 교환
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:

            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head
