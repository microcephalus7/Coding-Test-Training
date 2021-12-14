# 연결 리스트에 다른 연결 리스트 집어넣기
# 반복

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = end = list1

        for i in range(a-1):
            start = start.next

        for i in range(b + 1):
            end = end.next

        start.next = list2

        while list2.next:
            list2 = list2.next

        list2.next = end

        return list1
