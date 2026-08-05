from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        left = 0
        right = len(matrix[0])

        top = 0
        bottom = len(matrix)

        while left < right and top < bottom:
            # Traverse the top row from left to right
            for i in range(left, right):
                result.append(matrix[top][i])

            top += 1

            # Traverse the right column from top to bottom
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])

            right -= 1

            # Stop if there are no rows or columns remaining
            if not (left < right and top < bottom):
                break

            # Traverse the bottom row from right to left
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])

            bottom -= 1

            # Traverse the left column from bottom to top
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])

            left += 1

        return result