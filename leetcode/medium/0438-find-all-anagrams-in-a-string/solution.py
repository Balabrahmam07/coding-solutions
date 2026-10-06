class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p = sorted(p)
        count = []
        left = 0
        for right in range(len(p)-1, len(s)):
            if sorted(s[left:right+1]) == p:
                count.append(left)
            left += 1
        return count