# Majority Element

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an array `nums` of size `n`, return  *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

 

 **Example 1:** 

```
Input: nums = [3,2,3]
Output: 3

```

 **Example 2:** 

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2

```

 

 **Constraints:** 

- n == nums.length
- 1 <= n <= 5 * 104
- -109 <= nums[i] <= 109
- The input is generated such that a majority element will exist in the array.

 

 **Follow-up:**  Could you solve the problem in linear time and in `O(1)` space?

## Solution

**Language:** Python  
**Runtime:** 8 ms (beats 46.05%)  
**Memory:** 21.7 MB (beats 9.75%)  
**Submitted:** 2026-09-23T08:28:31.158Z  

```py
from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
```

---

[View on LeetCode](https://leetcode.com/problems/majority-element/)