# Find All Anagrams in a String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in  **any order**.

 

 **Example 1:** 

```
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

```

 **Example 2:** 

```
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

```

 

 **Constraints:** 

- 1 <= s.length, p.length <= 3 * 104
- s and p consist of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 23 ms (beats 96.39%)  
**Memory:** 19.5 MB (beats 96.25%)  
**Submitted:** 2026-10-06T06:31:26.885Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/)