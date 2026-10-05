# Permutation in String

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

 

 **Example 1:** 

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

```

 **Example 2:** 

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

```

 

 **Constraints:** 

- 1 <= s1.length, s2.length <= 104
- s1 and s2 consist of lowercase English letters.

## Solution

**Language:** Python  
**Runtime:** 15 ms (beats 80.30%)  
**Memory:** 19.2 MB (beats 97.75%)  
**Submitted:** 2026-10-05T10:34:20.640Z  

```py
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n = len(s1)
        s1_count = [0] * 26
        window_count = [0] * 26

        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1
        
        left = 0
        for right in range(len(s2)):
            window_count[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 > n:
                window_count[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if window_count == s1_count:
                return True
        return False
```

---

[View on LeetCode](https://leetcode.com/problems/permutation-in-string/)