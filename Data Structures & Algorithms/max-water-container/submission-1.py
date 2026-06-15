class Solution(object):
    def maxArea(self, height):
        max1 = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                width = j - i
                h = min(height[i], height[j])
                area = width * h

                max1 = max(max1, area)

        return max1