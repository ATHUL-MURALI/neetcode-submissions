# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        if list1:
            heapq.heappush(heap, (list1.val, 1, list1))
        if list2:
            heapq.heappush(heap, (list2.val, 2, list2))
        dummy = ListNode(0)
        curr = dummy
        while heap:
            _, idx, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
            curr.next = node
            curr = node
        return dummy.next
        


        # while list1 or list2:
        #     if list1:
        #         heapq.heappush(heap, (list1.val, 1, list1))
        #         list1 = list1.next
        #     if list2:
        #         heapq.heappush(heap, (list2.val, 2, list2))
        #         list2 = list2.next
        #     _, _, node = heapq.heappop(heap)
        #     curr.next = node
        #     curr = node


        