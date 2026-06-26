class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # move fast n steps ahead
        for i in range(n):
            fast = fast.next

        # move both until fast reaches last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # remove the nth node from end
        slow.next = slow.next.next

        return dummy.next