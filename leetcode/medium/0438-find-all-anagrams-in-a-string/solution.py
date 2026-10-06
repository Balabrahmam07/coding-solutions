class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_count = [0] * 26
        window_count = [0] * 26

        for i in p:
            p_count[ord(i) - ord('a')] += 1
        
        n = len(p)
        left = 0
        result = []

        for right in range(len(s)):
            window_count[ord(s[right]) - ord('a')] += 1

            if right - left + 1 > n:
                window_count[ord(s[left]) - ord('a')] -= 1
                left += 1
            
            if p_count == window_count:
                result.append(left)
        return result