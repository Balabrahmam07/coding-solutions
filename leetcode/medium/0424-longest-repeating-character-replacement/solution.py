class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = [0] * 26

        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):

           
            index = ord(s[right]) - ord('A')
            freq[index] += 1

            
            max_frequency = max(max_frequency, freq[index])

      
            window_length = right - left + 1
            replacements = window_length - max_frequency

   
            if replacements > k:
                freq[ord(s[left]) - ord('A')] -= 1
                left += 1

       
            max_length = max(max_length, right - left + 1)

        return max_length