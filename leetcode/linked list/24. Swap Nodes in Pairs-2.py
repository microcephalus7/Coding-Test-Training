# 모든 두 쌍의 노드 교환

# 반복 구조
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:

            # b 가 a(head) 를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prev 가 b 를 가리키도록 할당
            prev.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next

        return root.next
