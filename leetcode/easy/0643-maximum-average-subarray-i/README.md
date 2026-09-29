# Maximum Average Subarray I

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose  **length is equal to**  `k` that has the maximum average value and return  *this value*. Any answer with a calculation error less than `10-5` will be accepted.

 

 **Example 1:** 

```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

```

 **Example 2:** 

```
Input: nums = [5], k = 1
Output: 5.00000

```

 

 **Constraints:** 

- n == nums.length
- 1 <= k <= n <= 105
- -104 <= nums[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 47 ms (beats 92.37%)  
**Memory:** 29.3 MB (beats 36.98%)  
**Submitted:** 2026-09-29T06:33:16.036Z  

```py
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k,len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            if current_sum > max_sum:
                max_sum = current_sum
        return max_sum / k
            
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-average-subarray-i/)