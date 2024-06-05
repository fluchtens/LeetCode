from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1: str = ""
        val2: str = ""

        while(l1):
            val1 = val1 + str(l1.val)
            l1 = l1.next
        while(l2):
            val2 = val2 + str(l2.val)
            l2 = l2.next

        val1_str: str = str(val1)
        val1_nb: int = 0
        i: int = len(val1_str) - 1
        while (i >= 0):
            val1_nb = val1_nb * 10 + int(val1_str[i])
            i -= 1

        val2_str: str = str(val2)
        val2_nb: int = 0
        i: int = len(val2_str) - 1
        while (i >= 0):
            val2_nb = val2_nb * 10 + int(val2_str[i])
            i -= 1

        sum_nb: int = val1_nb + val2_nb
        sum_str = str(sum_nb)
        sum_len: int = len(sum_str) - 1
        ret = ListNode()
        ret_copy = ret
        while (sum_len >= 0):
            ret_copy.next = ListNode(int(sum_str[sum_len]))
            ret_copy = ret_copy.next
            sum_len -= 1

        return ret.next        
