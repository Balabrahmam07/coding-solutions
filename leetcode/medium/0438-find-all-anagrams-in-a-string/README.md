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
**Runtime:** 7215 ms (beats 5.01%)  
**Memory:** 19.8 MB (beats 68.95%)  
**Submitted:** 2026-10-06T06:15:01.388Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/find-all-anagrams-in-a-string/)