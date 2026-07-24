class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            # Odd-length palindromes
            left = i
            right = i
            count += self.countPali(s, left, right)

            # Even-length palindromes
            left = i
            right = i + 1
            count += self.countPali(s, left, right)

        return count

    def countPali(self, s: str, left: int, right: int) -> int:
        count = 0

        while (
            left >= 0
            and right < len(s)
            and s[left] == s[right]
        ):
            count += 1
            left -= 1
            right += 1

        return count