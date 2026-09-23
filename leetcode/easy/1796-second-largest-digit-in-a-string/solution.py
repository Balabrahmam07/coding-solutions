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
