# Second Largest Digit in a String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an alphanumeric string `s`, return  *the  **second largest**  numerical digit that appears in* `s` *, or* `-1` *if it does not exist*.

An  **alphanumeric**  string is a string consisting of lowercase English letters and digits.

 

 **Example 1:** 

```
Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

```

 **Example 2:** 

```
Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 

```

 

 **Constraints:** 

- 1 <= s.length <= 500
- s consists of only lowercase English letters and digits.

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.5 MB  
**Submitted:** 2026-09-23T09:11:50.351Z  

```py
class Solution:
    def secondHighest(self, s: str) -> int:
        largest = 0
        second = 0
        for i in s:
            if not i.isalpha():
                n = int(i)
                if n > largest:
                    second = largest
                    largest = n
                elif largest == second:
                    second = -1
                
        return second

```

---

[View on LeetCode](https://leetcode.com/problems/second-largest-digit-in-a-string/)