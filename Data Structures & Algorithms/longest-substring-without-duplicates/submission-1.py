class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = set()
        ans = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1

            chars.add(s[r])
            ans = max(ans, r - l + 1)

        return ans