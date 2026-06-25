class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # moves 1 step
            fast = fast.next.next     # moves 2 steps

            if slow == fast:          # same node, not same value
                return True

        return False