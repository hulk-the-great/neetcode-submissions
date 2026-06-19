class Solution(object):
    def isValid(self, s):
        stack = []

        matching = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    return False

                top = stack.pop()

                if top != matching[char]:
                    return False

        return len(stack) == 0