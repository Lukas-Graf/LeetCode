from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result: ListNode = ListNode()
        ptr = result
        rest: int = 0

        while l1 or l2 or rest:
            addend1: int = l1.val if l1 else 0
            addend2: int = l2.val if l2 else 0
            total: int = addend1 + addend2 + rest

            rest: int = total // 10
            remainder: int = total % 10
            ptr.next = ListNode(remainder)

            ptr = ptr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next
